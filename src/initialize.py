from db_connection import connect


def create_tables(conn):
    """Luo tietokantataulut.
    
    Args:
        conn: Tietokantayhteys
    """


    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Cards (
                   id INTEGER PRIMARY KEY,
                   Pokémon TEXT,
                   Pokédex_Number INTEGER,
                   Expansion TEXT,
                   Release_Date DATE,
                   UNIQUE(Pokémon, Pokédex_Number, Expansion, Release_Date))""")
    conn.commit()


def initialize(conn=None):
    """Avaa tietokantayhteyden ja luo tietokantataulut.

    Args:
        conn: SQLite-yhteys. Uusi yhteys luodaan, jos None.
    """


    conn = conn or connect()
    create_tables(conn)
