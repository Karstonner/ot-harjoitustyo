import unittest
from repositories.card_repository import CardRepository
from initialize import initialize
from entities.card import Card
from tests.test_db import get_test_connection

class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.conn = get_test_connection()
        initialize(self.conn)
        self.repo = CardRepository(conn=self.conn)
        self.repo.clear()

    def tearDown(self):
        self.repo.clear()
        self.conn.close()

    def test_empty_database(self):
        self.assertEqual(len(self.repo.get_cards()), 0)

    def test_new_card(self):
        success = self.repo.new_card("Bulbasaur", 1, "Base Set", "1999-01-09")
        self.assertTrue(success)
        cards = self.repo.get_cards()
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0].pokemon, "Bulbasaur")
        self.assertEqual(cards[0].pokedex_number, 1)
        self.assertEqual(cards[0].expansion, "Base Set")
        self.assertEqual(cards[0].release_date, "1999-01-09")

    def test_get_cards(self):
        self.repo.new_card("Bulbasaur", 1, "Base Set", "1999-01-09")
        self.repo.new_card("Charmander", 4, "Base Set", "1999-01-09")
        cards = self.repo.get_cards()
        self.assertEqual(len(cards), 2)
        pokemon_names = [card.pokemon for card in cards]
        self.assertIn("Bulbasaur", pokemon_names)
        self.assertIn("Charmander", pokemon_names)

    def test_remove_card(self):
        self.repo.new_card("Bulbasaur", 1, "Base Set", "1999-01-09")
        cards = self.repo.get_cards()
        self.assertEqual(len(cards), 1)
        success = self.repo.remove_card(cards[0].pokemon, cards[0].pokedex_number, 
                                       cards[0].expansion, cards[0].release_date)
        self.assertTrue(success)
        self.assertEqual(len(self.repo.get_cards()), 0)

    def test_remove_nonexistent_card(self):
        success = self.repo.remove_card("Bulbasaur", 1, "Base Set", "1999-01-09")
        self.assertFalse(success)
        self.assertEqual(len(self.repo.get_cards()), 0)

    def test_clear_database(self):
        self.repo.new_card("Bulbasaur", 1, "Base Set", "1999-01-09")
        self.repo.new_card("Charmander", 4, "Base Set", "1999-01-09")
        self.assertEqual(len(self.repo.get_cards()), 2)
        self.repo.clear()
        self.assertEqual(len(self.repo.get_cards()), 0)

    def test_new_card_invalid_date(self):
        success = self.repo.new_card("Bulbasaur", 1, "Base Set", "invalid-date")
        self.assertFalse(success)
        self.assertEqual(len(self.repo.get_cards()), 0)

if __name__ == "__main__":
    unittest.main()