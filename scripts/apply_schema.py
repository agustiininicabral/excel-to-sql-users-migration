from pathlib import Path
import os
import mysql.connector

def main():
    connection=mysql.connector.connect(
        host=os.getenv("DB_HOST","127.0.0.1"),
        port=int(os.getenv("DB_PORT","3306")),
        user=os.getenv("DB_USER","root"),
        password=os.getenv("DB_PASSWORD",""),
    )
    try:
        cursor=connection.cursor()
        source=Path("sql/001_create_schema.sql").read_text(encoding="utf-8")
        for statement in source.split(";"):
            statement="\n".join(line for line in statement.splitlines()
                                if not line.lstrip().startswith("--")).strip()
            if statement:
                cursor.execute(statement)
        connection.commit()
        print("MySQL schema applied successfully.")
    finally:
        connection.close()

if __name__=="__main__": main()
