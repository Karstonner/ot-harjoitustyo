import unittest
from repositories.card_repository import CardRepository as cr
from initialize import initialize


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.repo = cr()
        self.repo.clear()
        initialize()
    
    def test_empty_database(self):
        self.assertEqual(len(self.repo.get_cards()), 0)

    def test_new_card(self):
        self.repo.new_card(
            "Bulbasaur", 1, "Base Set", 1999-1-9)
        cards = self.repo.get_cards()
        self.assertEqual(cards[0][0], "Bulbasaur")
        self.assertEqual(cards[0][2], "Base Set")

    def test_remove_card(self):
        self.repo.new_card(
            "Bulbasaur", 1, "Base Set", 1999-1-9)
        cards = self.repo.get_cards()
        self.repo.remove_card(
            cards[0][0], cards[0][1], cards[0][2], cards[0][3])
        cards = self.repo.get_cards()
        self.assertEqual(len(cards), 0)