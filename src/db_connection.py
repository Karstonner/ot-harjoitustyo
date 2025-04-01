import sqlite3
from config import DB_FILE_PATH

connection = sqlite3.connect(DB_FILE_PATH)
connection.row_factory = sqlite3.Row

def connect():
    return connection