#from entities.card import Card
from db_connection import connect

class CardRepository:
    def __init__(self, conn):
        self.conn = conn
        
    def get_cards(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""SELECT * FROM Cards""")
            result = cursor.fetchall()
            return result
        except:
            return False
    
    def new_card(self, pokemon, dex_number, expansion, release_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO Cards (
            Pokémon, Pokédex_Number, Expansion, Release_Date)
            values (?, ?, ?, ?)""",
            (pokemon, dex_number, expansion, release_date))
        self.conn.commit()
        return True

    def clear(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""DELETE FROM Cards""")
            self.conn.commit()
        except:
            pass

card_repository = CardRepository(connect())