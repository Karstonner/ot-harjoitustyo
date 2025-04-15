import unittest
import tkinter as tk
from gui import UI
from initialize import initialize
from repositories.card_repository import CardRepository


class TestUI(unittest.TestCase):
    def setUp(self):
        initialize()
        self.root = tk.Tk()
        self.ui = UI(self.root)
        self.cards = [
            ("Bulbasaur", 1, "Base", "1999-01-09"),
            ("Charmander", 4, "Base", "1999-01-09"),
            ("Squirtle", 7, "Base", "1999-01-09")]

    def tearDown(self):
        self.root.destroy()
    
    def test_window_title(self):
        self.assertEqual(self.root.title(), "Pokemon Card App")
    
    def test_window_size(self):
        self.assertEqual(self.root.minsize(), (900,600))
    
    def test_heading_exists(self):
        found = False
        for i in self.root.winfo_children():
            if isinstance(i, tk.Label):
                if i["text"] == "Your cards":
                    found = True
        self.assertTrue(found)
    
    def test_sort_by_name_ascending(self):
        sorted_cards = self.ui.sort_cards(self.cards, 0, True)
        self.assertEqual(sorted_cards[0][0], "Bulbasaur")
        self.assertEqual(sorted_cards[1][0], "Charmander")
        self.assertEqual(sorted_cards[2][0], "Squirtle")
    
    def test_sort_by_dex_descending(self):
        sorted_cards = self.ui.sort_cards(self.cards, 1, False)
        self.assertEqual(sorted_cards[0][1], 7)
        self.assertEqual(sorted_cards[1][1], 4)
        self.assertEqual(sorted_cards[2][1], 1)