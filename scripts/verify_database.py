import os
import mysql.connector

def main():
    connection=mysql.connector.connect(
        host=os.getenv("DB_HOST","127.0.0.1"),
        port=int(os.getenv("DB_PORT","3306")),
        database=os.getenv("DB_NAME","excel_migration"),
        user=os.getenv("DB_USER","root"),
        password=os.getenv("DB_PASSWORD",""),
    )
    try:
        cursor=connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        total=cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM users WHERE email <> LOWER(email) OR first_name='' OR last_name=''")
        invalid=cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM (SELECT email FROM users GROUP BY email HAVING COUNT(*)>1) d")
        duplicates=cursor.fetchone()[0]
        assert total==26, f"Expected 26 users, got {total}"
        assert invalid==0, f"Found {invalid} invalid required values"
        assert duplicates==0, f"Found {duplicates} duplicate emails"
        print(f"MySQL integration verified: {total} users, no invalid required values, no duplicate emails.")
    finally:
        connection.close()

if __name__=="__main__": main()
