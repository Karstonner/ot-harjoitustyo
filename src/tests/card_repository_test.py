import unittest
from repositories.card_repository import card_repository
from initialize import initialize


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        card_repository.clear()
        initialize()
    
    def test_empty_database(self):
        self.assertEqual(len(card_repository.get_cards()), 0)

    def test_new_card(self):
        card_repository.new_card(
            "Bulbasaur", 1, "Base Set", 1999-1-9)
        cards = card_repository.get_cards()
        self.assertEqual(cards[0][1], "Bulbasaur")
        self.assertEqual(cards[0][3], "Base Set")

    def test_remove_card(self):
        card_repository.new_card(
            "Bulbasaur", 1, "Base Set", 1999-1-9)
        cards = card_repository.get_cards()
        card_repository.remove_card(
            cards[0][1], cards[0][2], cards[0][3], cards[0][4])
        cards = card_repository.get_cards()
        self.assertEqual(len(cards), 0)