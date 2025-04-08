from entities.card import Card
from db_connection import connect


class CardRepository:
    def __init__(self, conn):
        self.conn = conn
        self.card_list = []

    def get_cards(self):
        return self.card_list

    def new_card(self, pokemon, dex_number, expansion, release_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO Cards (
            Pokémon, Pokédex_Number, Expansion, Release_Date)
            values (?, ?, ?, ?)""",
            (pokemon, dex_number, expansion, release_date))
        self.conn.commit()
        self.card_list.append(Card(pokemon, dex_number, expansion, release_date))
        return True

    def remove_card(self, pokemon, dex_number, expansion, release_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """DELETE FROM Cards WHERE 
            Pokémon = ? AND Pokédex_Number = ? AND Expansion = ? AND Release_Date = ?""",
            (pokemon, dex_number, expansion, release_date)
        )
        self.conn.commit()
        #self.card_list.remove(Card(pokemon, dex_number, expansion, release_date))

    def clear(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""DELETE FROM Cards""")
            self.conn.commit()
        except:
            pass


card_repository = CardRepository(connect())
