from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    database: str
    user: str
    password: str

    @classmethod
    def from_env(cls):
        return cls(os.getenv("DB_HOST","127.0.0.1"), int(os.getenv("DB_PORT","3306")),
                   os.getenv("DB_NAME","excel_migration"), os.getenv("DB_USER","root"),
                   os.getenv("DB_PASSWORD",""))
