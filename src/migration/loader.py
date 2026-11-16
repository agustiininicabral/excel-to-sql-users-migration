import mysql.connector
from migration.config import DatabaseConfig

INSERT_SQL = """INSERT INTO users
(source_id,first_name,last_name,email,phone,created_at,status)
VALUES (%s,%s,%s,%s,%s,%s,%s)
ON DUPLICATE KEY UPDATE first_name=VALUES(first_name),last_name=VALUES(last_name),
phone=VALUES(phone),created_at=VALUES(created_at),status=VALUES(status)"""

def load_users(frame, config: DatabaseConfig) -> int:
    if frame.empty: return 0
    connection = mysql.connector.connect(host=config.host,port=config.port,database=config.database,
                                         user=config.user,password=config.password)
    try:
        cursor = connection.cursor()
        values = [(int(r.source_id),r.first_name,r.last_name,r.email,r.phone,r.created_at,r.status)
                  for r in frame.itertuples(index=False)]
        cursor.executemany(INSERT_SQL, values)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
