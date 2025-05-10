from db_connection import connect


def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Cards (
                   id INTEGER PRIMARY KEY,
                   Pokémon TEXT,
                   Pokédex_Number INTEGER,
                   Expansion TEXT,
                   Release_Date DATE)""")
    conn.commit()


def initialize():
    conn = connect()
    create_tables(conn)

if __name__ == "__main__":
    initialize()
