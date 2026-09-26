import psycopg

from config import settings
class Database:
    def __init__(self):
        self.conn = psycopg.connect(settings.DATABASE_URL)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()