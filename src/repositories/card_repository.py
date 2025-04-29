import sqlite3
from db_connection import connect


class CardRepository:
    """Repositorio, joka pitää yllä olemassa olevat kortit."""

    def __init__(self):
        """Luokan konstruktori.
        
        Args:
            conn:
                Luo yhteyden tietokantaamme.
        """
        self.conn = connect()

    def get_cards(self):
        """Hakee kaikki omistetut kortit tietokannasta hallitavaan muotoon."""
        cursor = self.conn.cursor()
        cursor.execute("""SELECT Pokémon, Pokédex_Number, Expansion, Release_Date FROM Cards""")
        result = cursor.fetchall()
        return result

    def new_card(self, pokemon, dex_number, expansion, release_date):
        """Luo uuden kortin tietokantaan."""
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO Cards (
            Pokémon, Pokédex_Number, Expansion, Release_Date)
            values (?, ?, ?, ?)""",
            (pokemon, dex_number, expansion, release_date))
        self.conn.commit()

    def remove_card(self, pokemon, dex_number, expansion, release_date):
        """Poistaa kortin tietokannasta."""
        cursor = self.conn.cursor()
        cursor.execute(
            """DELETE FROM Cards WHERE 
            Pokémon = ? AND Pokédex_Number = ? AND Expansion = ? AND Release_Date = ?""",
            (pokemon, dex_number, expansion, release_date)
        )
        self.conn.commit()

    def clear(self):
        """Tyhjentää koko tietokannan, jos sellainen on olemassa. Ei kuitenkaan poista sitä."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""DELETE FROM Cards""")
            self.conn.commit()
        except sqlite3.OperationalError:
            pass
