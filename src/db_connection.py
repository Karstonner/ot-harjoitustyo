import sqlite3
from config import DB_FILE_PATH

def connect():
    connection = sqlite3.connect(DB_FILE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
