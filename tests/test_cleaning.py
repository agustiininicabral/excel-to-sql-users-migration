import pandas as pd
import pytest
from migration.cleaning import clean_users,normalize_email,normalize_text,parse_created_at

def test_email_normalization():
    assert normalize_email(" USER@Example.COM ")=="user@example.com"

def test_blank_text_becomes_none():
    assert normalize_text("  ") is None

def test_date_formats():
    assert str(parse_created_at("15/02/2024"))=="2024-02-15"
    assert str(parse_created_at("2024-03-03"))=="2024-03-03"

def test_rejections_and_deduplication():
    frame=pd.DataFrame([
      [1," Ana ","Paz","ANA@EXAMPLE.COM ","123","2024-01-01","ACTIVE"],
      [2,"Ana","Paz","ana@example.com","123","2024-01-01","active"],
      [3,"Luis","Ríos","bad-email","123","2024-01-01","active"],
      [4,"Eva","Sol","eva@example.com","123","bad-date","active"],
      [5,"Noe","Mar","noe@example.com","123","2024-01-01","unknown"],
    ],columns=["source_id","first_name","last_name","email","phone","created_at","status"])
    accepted,rejected=clean_users(frame)
    assert len(accepted)==1
    assert accepted.iloc[0].email=="ana@example.com"
    assert set(rejected.rejection_reason)=={"duplicate_email","invalid_email","invalid_created_at","invalid_status"}

def test_missing_columns_fail_fast():
    with pytest.raises(ValueError,match="Missing required columns"):
        clean_users(pd.DataFrame({"email":["x@example.com"]}))
