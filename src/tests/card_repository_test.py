import unittest
from repositories.card_repository import card_repository
from initialize import initialize

class TestCardRepository(unittest.TestCase):
    def setUp(self):
        card_repository.clear()
        initialize()

    def test_new_card(self):
        card_repository.new_card(
            "Bulbasaur", 1, "Base Set", 1999-1-9)
        cards = card_repository.get_cards()
        self.assertEqual(cards[0][1], "Bulbasaur")
        self.assertEqual(cards[0][3], "Base Set")