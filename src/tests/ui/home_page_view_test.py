import unittest
import tkinter as tk
from unittest.mock import MagicMock
from ui.home_page_view import HomePage
from repositories.card_repository import CardRepository
from entities.card import Card
from initialize import initialize
from tests.test_db import get_test_connection

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.conn = get_test_connection()
        initialize(self.conn)
        self.card_repo = CardRepository(conn=self.conn)
        self.card_repo.clear()
        self.cards = [
            Card("Bulbasaur", 1, "Base Set", "1999-01-09"),
            Card("Charmander", 4, "Base Set", "1999-01-09"),
            Card("Squirtle", 7, "Base Set", "1999-01-09"),
            Card("Ampharos", 181, "Neo Genesis", "2000-02-04")
        ]
        for card in self.cards:
            self.card_repo.new_card(card.pokemon, card.pokedex_number, card.expansion, card.release_date)
        
        self.root = tk.Tk()
        self.controller = MagicMock()
        self.ui = HomePage(self.root, self.controller, self.card_repo)
        self.root.update()
        self.ui.display_cards()
    
    def tearDown(self):
        self.card_repo.clear()
        self.ui.destroy()
        self.root.destroy()
        self.conn.close()
    
    def test_heading_exists(self):
        found = False
        for widget in self.ui.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, tk.Label) and child["text"] == "Your cards":
                    found = True
        self.assertTrue(found)
    
    def test_add_button_exists(self):
        found = False
        for widget in self.ui.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, tk.Button) and child["text"] == "Add card":
                    found = True
                    child.invoke()
        self.assertTrue(found)
        self.controller.show_frame.assert_called_with("NewCard")
    
    def test_card_headers_exist(self):
        headers = ["Pokémon", "Dex #", "Expansion", "Release Date"]
        found_headers = set()
        for widget in self.ui.card_header_frame.winfo_children():
            if (isinstance(widget, tk.Label) and 
                widget.grid_info().get("row") == 0 and
                widget.grid_info().get("column") in [0, 1, 2, 3] and
                "card" not in widget["text"].lower()):
                found_headers.add(widget["text"])
        self.assertEqual(sorted(found_headers), sorted(headers))
    
    def test_display_cards(self):
        displayed_cards = []
        for row in self.ui.card_widgets:
            pokemon = row[0]["text"]
            displayed_cards.append(pokemon)
        self.assertEqual(len(displayed_cards), 4)
        self.assertIn("Bulbasaur", displayed_cards)
        self.assertIn("Charmander", displayed_cards)
        self.assertIn("Squirtle", displayed_cards)
        self.assertIn("Ampharos", displayed_cards)
    
    def test_card_count_label(self):
        found = False
        for widget in self.ui.card_header_frame.winfo_children():
            if isinstance(widget, tk.Label) and widget["text"] == "4 cards owned":
                found = True
        self.assertTrue(found)
    
    def test_sort_by_name_ascending(self):
        self.ui.setup_sorting(0)
        self.root.update()
        displayed_cards = [row[0]["text"] for row in self.ui.card_widgets]
        self.assertEqual(displayed_cards, ["Ampharos", "Bulbasaur", "Charmander", "Squirtle"])
    
    def test_sort_by_dex_descending(self):
        self.ui.setup_sorting(1)
        self.ui.setup_sorting(1)
        self.root.update()
        displayed_cards = [row[1]["text"] for row in self.ui.card_widgets]
        self.assertEqual(displayed_cards, [181, 7, 4, 1])
    
    def test_sort_by_set_descending(self):
        self.ui.setup_sorting(2)
        self.ui.setup_sorting(2)
        self.root.update()
        displayed_cards = [row[2]["text"] for row in self.ui.card_widgets]
        self.assertEqual(displayed_cards, ["Neo Genesis", "Base Set", "Base Set", "Base Set"])
    
    def test_sort_by_date_ascending(self):
        self.ui.setup_sorting(3)
        self.root.update()
        displayed_cards = [row[3]["text"] for row in self.ui.card_widgets]
        self.assertEqual(displayed_cards, ["1999-01-09", "1999-01-09", "1999-01-09", "2000-02-04"])
        pokemon = [row[0]["text"] for row in self.ui.card_widgets[:3]]
        self.assertEqual(pokemon, ["Bulbasaur", "Charmander", "Squirtle"])
    
    def test_remove_card(self):
        with unittest.mock.patch("tkinter.messagebox.askquestion", return_value="yes"):
            remove_button = self.ui.card_widgets[0][-1]
            remove_button.invoke()
        cards = self.card_repo.get_cards()
        self.assertEqual(len(cards), 3)
        displayed_cards = [row[0]["text"] for row in self.ui.card_widgets]
        self.assertEqual(len(displayed_cards), 3)


if __name__ == "__main__":
    unittest.main()