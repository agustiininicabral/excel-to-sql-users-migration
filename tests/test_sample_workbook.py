from pathlib import Path
import subprocess,sys
from migration.cleaning import clean_users,load_workbook

ROOT=Path(__file__).resolve().parents[1]

def test_generated_workbook_and_quality_cases():
    workbook=ROOT/"data/source/users_source.xlsx"
    if not workbook.exists():
        subprocess.run([sys.executable,"scripts/generate_sample_workbook.py"],cwd=ROOT,check=True)
    raw=load_workbook(str(workbook))
    accepted,rejected=clean_users(raw)
    assert len(raw)==32
    assert len(accepted)+len(rejected)==len(raw)
    reasons="|".join(rejected.rejection_reason)
    assert "duplicate_email" in reasons
    assert "invalid_email" in reasons
    assert "invalid_status" in reasons
