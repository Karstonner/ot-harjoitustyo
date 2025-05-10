import sqlite3
from db_connection import connect
from initialize import create_tables
from entities.card import Card


class CardRepository:
    """Repositorio, joka pitää yllä olemassa olevat kortit.
    """

    def __init__(self):
        """Luokan konstruktori.
        
        Args:
            conn:
                Luo yhteyden tietokantaamme.
            create_tables:
                Luo taulut, jos niitä ei ole vielä olemassa.
        """


        self.conn = connect()
        create_tables(self.conn)

    def get_cards(self):
        """Hakee kaikki omistetut kortit tietokannasta hallitavaan muotoon.
        """


        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT id, Pokémon, Pokédex_Number, Expansion, Release_Date FROM Cards""")
            rows = cursor.fetchall()
            return [Card(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        except Exception as e:
            print(f"Error fetching cards: {e}")
            return []

    def new_card(self, pokemon, dex_number, expansion, release_date):
        """Luo uuden kortin tietokantaan.
        """


        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO Cards (
                Pokémon, Pokédex_Number, Expansion, Release_Date)
                values (?, ?, ?, ?)""",
                (pokemon, dex_number, expansion, release_date))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting card: {e}")
            return False

    def remove_card(self, pokemon, dex_number, expansion, release_date):
        """Poistaa kortin tietokannasta.
        """


        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """DELETE FROM Cards WHERE 
                Pokémon = ? AND Pokédex_Number = ? AND Expansion = ? AND Release_Date = ?""",
                (pokemon, dex_number, expansion, release_date)
            )
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error removing card: {e}")
            return False

    def clear(self):
        """Tyhjentää koko tietokannan, jos sellainen on olemassa. Ei kuitenkaan poista sitä.
        """


        cursor = self.conn.cursor()
        try:
            cursor.execute("""DELETE FROM Cards""")
            self.conn.commit()
        except sqlite3.OperationalError:
            pass
