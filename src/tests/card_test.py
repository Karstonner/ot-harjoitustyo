import unittest
from entities.card import Card

class TestCard(unittest.TestCase):
    def test_card_initialization(self):
        card = Card("Bulbasaur", 1, "Base Set", "1999-01-09", id=1)
        self.assertEqual(card.pokemon, "Bulbasaur")
        self.assertEqual(card.pokedex_number, 1)
        self.assertEqual(card.expansion, "Base Set")
        self.assertEqual(card.release_date, "1999-01-09")
        self.assertEqual(card.id, 1)

    def test_card_initialization_no_id(self):
        card = Card("Bulbasaur", 1, "Base Set", "1999-01-09")
        self.assertIsNone(card.id)

    def test_card_repr(self):
        card = Card("Bulbasaur", 1, "Base Set", "1999-01-09", id=1)
        expected = "Card(id=1, pokemon=Bulbasaur, pokedex_number=1, expansion=Base Set, release_date=1999-01-09)"
        self.assertEqual(repr(card), expected)

    def test_card_repr_no_id(self):
        card = Card("Bulbasaur", 1, "Base Set", "1999-01-09")
        expected = "Card(id=None, pokemon=Bulbasaur, pokedex_number=1, expansion=Base Set, release_date=1999-01-09)"
        self.assertEqual(repr(card), expected)

if __name__ == "__main__":
    unittest.main()