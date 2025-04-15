#from entities.card import Card
from db_connection import connect


class CardRepository:
    def __init__(self):
        self.conn = connect()

    def get_cards(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT Pokémon, Pokédex_Number, Expansion, Release_Date FROM Cards""")
        result = cursor.fetchall()
        return result

    def new_card(self, pokemon, dex_number, expansion, release_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO Cards (
            Pokémon, Pokédex_Number, Expansion, Release_Date)
            values (?, ?, ?, ?)""",
            (pokemon, dex_number, expansion, release_date))
        self.conn.commit()

    def remove_card(self, pokemon, dex_number, expansion, release_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """DELETE FROM Cards WHERE 
            Pokémon = ? AND Pokédex_Number = ? AND Expansion = ? AND Release_Date = ?""",
            (pokemon, dex_number, expansion, release_date)
        )
        self.conn.commit()

    def clear(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""DELETE FROM Cards""")
            self.conn.commit()
        except:
            pass