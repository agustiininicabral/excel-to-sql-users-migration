from __future__ import annotations
import re
from typing import Any
import pandas as pd

ALLOWED_STATUSES = {"active", "inactive", "pending"}
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

def normalize_text(value: Any) -> str | None:
    if pd.isna(value): return None
    result = str(value).strip()
    return result or None

def normalize_email(value: Any) -> str | None:
    value = normalize_text(value)
    return value.lower() if value else None

def parse_created_at(value: Any):
    if value is None or pd.isna(value): return None
    parsed = pd.to_datetime(value, dayfirst=True, errors="coerce")
    return None if pd.isna(parsed) else parsed.date()

def clean_users(frame: pd.DataFrame):
    required = {"source_id","first_name","last_name","email","phone","created_at","status"}
    missing = required.difference(frame.columns)
    if missing: raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    accepted, rejected, seen = [], [], set()
    for row in frame.to_dict(orient="records"):
        record = {
            "source_id": int(row["source_id"]),
            "first_name": normalize_text(row["first_name"]),
            "last_name": normalize_text(row["last_name"]),
            "email": normalize_email(row["email"]),
            "phone": normalize_text(row["phone"]),
            "created_at": parse_created_at(row["created_at"]),
            "status": (normalize_text(row["status"]) or "").lower(),
        }
        reasons = []
        if not record["first_name"]: reasons.append("missing_first_name")
        if not record["last_name"]: reasons.append("missing_last_name")
        if not record["email"] or not EMAIL_PATTERN.fullmatch(record["email"]): reasons.append("invalid_email")
        if not record["created_at"]: reasons.append("invalid_created_at")
        if record["status"] not in ALLOWED_STATUSES: reasons.append("invalid_status")
        if not reasons and record["email"] in seen: reasons.append("duplicate_email")
        if reasons: rejected.append({**record,"rejection_reason":"|".join(reasons)})
        else:
            seen.add(record["email"])
            accepted.append(record)
    return pd.DataFrame(accepted), pd.DataFrame(rejected)

def load_workbook(path: str):
    return pd.read_excel(path, sheet_name="Users", dtype={"phone":"string"})
