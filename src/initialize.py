from db_connection import connect


def clear(conn):
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE if EXISTS Cards;""")
    conn.commit()


def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Cards (
                   id INTEGER PRIMARY KEY,
                   Pokémon TEXT,
                   Pokédex_Number INTEGER,
                   Expansion TEXT,
                   Release_Date DATE)""")
    conn.commit()


def initialize():
    conn = connect()

    clear(conn)
    create_tables(conn)


initialize()
