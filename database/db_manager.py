import psycopg2
from psycopg2.extras import DictCursor

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="tecido_db",
            user="usuario",
            password="senha",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)

    def insert_data(self, table, data):
        keys = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def fetch_data(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

db = DatabaseManager()
