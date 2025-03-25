import unittest
from maksukortti import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(1000)
    
    def test_constructor_sets_up_balance(self):
        self.assertEqual(str(self.card), "The card has 10.00 euros")
    
    def test_eating_cheap_reduces_balance(self):
        self.card.eat_cheap()

        self.assertEqual(self.card.balance_in_euros(), 7.5)
    
    def test_eat_tasty_reduces_balance(self):
        self.card.eat_tasty()

        self.assertEqual(self.card.balance_in_euros(), 6.0)
    
    def test_eat_cheap_does_not_go_negative(self):
        card = Card(200)
        card.eat_cheap()

        self.assertEqual(card.balance_in_euros(), 2.0)
    
    def test_eat_tasty_does_not_go_negative(self):
        card = Card(200)
        card.eat_tasty()

        self.assertEqual(card.balance_in_euros(), 2.0)
    
    def test_card_can_be_loaded(self):
        self.card.load_money(2500)

        self.assertEqual(self.card.balance_in_euros(), 35.0)
    
    def test_card_balance_does_not_overflow(self):
        self.card.load_money(20000)

        self.assertEqual(self.card.balance_in_euros(), 150.0)
    
    def test_card_can_not_be_loaded_negatively(self):
        self.card.load_money(-500)

        self.assertEqual(self.card.balance_in_euros(), 10.0)
    
    def test_can_barely_afford_cheap(self):
        card = Card(250)
        card.eat_cheap()

        self.assertEqual(card.balance_in_euros(), 0)
    
    def test_can_barely_afford_tasty(self):
        card = Card(400)
        card.eat_tasty()

        self.assertEqual(card.balance_in_euros(), 0)