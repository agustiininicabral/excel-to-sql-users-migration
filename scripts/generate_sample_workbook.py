from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
source=ROOT/"data/source/users_source.csv"
target=ROOT/"data/source/users_source.xlsx"

def main():
    frame=pd.read_csv(source,dtype={"phone":"string"})
    with pd.ExcelWriter(target,engine="openpyxl") as writer:
        frame.to_excel(writer,sheet_name="Users",index=False)
    print(f"Generated {target} with {len(frame)} rows")

if __name__=="__main__": main()
