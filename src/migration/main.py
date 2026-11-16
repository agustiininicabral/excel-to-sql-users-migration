import argparse
from pathlib import Path
from migration.cleaning import clean_users, load_workbook
from migration.config import DatabaseConfig
from migration.loader import load_users

ROOT = Path(__file__).resolve().parents[2]

def main():
    parser=argparse.ArgumentParser(description="Clean and migrate users from Excel to MySQL.")
    parser.add_argument("--input",default=str(ROOT/"data/source/users_source.xlsx"))
    parser.add_argument("--dry-run",action="store_true")
    args=parser.parse_args()
    source=Path(args.input)
    if not source.exists():
        raise FileNotFoundError(f"Workbook not found: {source}. Run scripts/generate_sample_workbook.py first.")
    raw=load_workbook(str(source))
    accepted,rejected=clean_users(raw)
    reports=ROOT/"reports"
    reports.mkdir(exist_ok=True)
    accepted.to_csv(reports/"accepted_users.csv",index=False)
    rejected.to_csv(reports/"rejected_users.csv",index=False)
    print(f"Source rows: {len(raw)}")
    print(f"Accepted rows: {len(accepted)}")
    print(f"Rejected rows: {len(rejected)}")
    if not rejected.empty: print(rejected["rejection_reason"].value_counts().to_string())
    if args.dry_run:
        print("DRY RUN: no database connection was opened.")
        return 0
    print(f"MySQL affected-row count: {load_users(accepted,DatabaseConfig.from_env())}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
