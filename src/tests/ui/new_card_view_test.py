import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch
from ui.new_card_view import NewCard
from repositories.card_repository import CardRepository
from initialize import initialize
from tests.test_db import get_test_connection

class TestNewCard(unittest.TestCase):
    def setUp(self):
        self.conn = get_test_connection()
        initialize(self.conn)
        self.card_repo = CardRepository(conn=self.conn)
        self.card_repo.clear()
        self.root = tk.Tk()
        self.controller = MagicMock()
        self.ui = NewCard(self.root, self.controller, self.card_repo)
        self.root.update()

    def tearDown(self):
        self.card_repo.clear()
        self.ui.destroy()
        self.root.destroy()
        self.conn.close()

    def test_form_fields_exist(self):
        form_frame = self.ui.winfo_children()[0]
        labels = [w["text"] for w in form_frame.winfo_children() if isinstance(w, tk.Label)]
        self.assertIn("Pokemon's Name:", labels)
        self.assertIn("Dex Number:", labels)
        self.assertIn("Card Set:", labels)
        self.assertIn("Release Date:", labels)
        entries = [w for w in form_frame.winfo_children() if isinstance(w, tk.Entry)]
        self.assertEqual(len(entries), 4)
        buttons = [w["text"] for w in form_frame.winfo_children() if isinstance(w, tk.Button)]
        self.assertIn("Submit", buttons)
        self.assertIn("Cancel", buttons)

    def test_form_placeholders(self):
        self.assertEqual(self.ui.name_entry.get(), "Esim: Bulbasaur")
        self.assertEqual(self.ui.dex_entry.get(), "1 - 1025")
        self.assertEqual(self.ui.set_entry.get(), "Esim: Base Set")
        self.assertEqual(self.ui.date_entry.get(), "YYYY-MM-DD")
        self.assertEqual(self.ui.name_entry.cget("fg"), "grey")

    def test_focus_in_clears_placeholders(self):
        self.ui.name_entry.focus()
        self.ui.name_focus_in(None)
        self.assertEqual(self.ui.name_entry.get(), "")
        self.assertEqual(self.ui.name_entry.cget("fg"), "black")

    @patch("tkinter.messagebox.showerror")
    def test_submit_valid_card(self, mock_showerror):
        self.ui.name_entry.delete(0, tk.END)
        self.ui.name_entry.insert(0, "Bulbasaur")
        self.ui.dex_entry.delete(0, tk.END)
        self.ui.dex_entry.insert(0, "1")
        self.ui.set_entry.delete(0, tk.END)
        self.ui.set_entry.insert(0, "Base Set")
        self.ui.date_entry.delete(0, tk.END)
        self.ui.date_entry.insert(0, "1999-01-09")
        
        self.ui.submit_card()
        cards = self.card_repo.get_cards()
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0].pokemon, "Bulbasaur")
        self.assertEqual(cards[0].pokedex_number, 1)
        self.assertEqual(cards[0].expansion, "Base Set")
        self.assertEqual(cards[0].release_date, "1999-01-09")
        self.controller.show_frame.assert_called_with("HomePage")
        mock_showerror.assert_not_called()

    @patch("tkinter.messagebox.showerror")
    def test_submit_empty_fields(self, mock_showerror):
        self.ui.name_entry.delete(0, tk.END)
        self.ui.dex_entry.delete(0, tk.END)
        self.ui.set_entry.delete(0, tk.END)
        self.ui.date_entry.delete(0, tk.END)
        self.ui.submit_card()
        mock_showerror.assert_called_with("Error", "All fields are required.")
        self.assertEqual(len(self.card_repo.get_cards()), 0)

    @patch("tkinter.messagebox.showerror")
    def test_submit_invalid_dex_number(self, mock_showerror):
        self.ui.name_entry.delete(0, tk.END)
        self.ui.name_entry.insert(0, "Bulbasaur")
        self.ui.dex_entry.delete(0, tk.END)
        self.ui.dex_entry.insert(0, "9999")
        self.ui.set_entry.delete(0, tk.END)
        self.ui.set_entry.insert(0, "Base Set")
        self.ui.date_entry.delete(0, tk.END)
        self.ui.date_entry.insert(0, "1999-01-09")
        
        self.ui.submit_card()
        mock_showerror.assert_called_with("Error", "Dex Number must be between 1 and 1025.")
        self.assertEqual(len(self.card_repo.get_cards()), 0)

    @patch("tkinter.messagebox.showerror")
    def test_submit_invalid_date_format(self, mock_showerror):
        self.ui.name_entry.delete(0, tk.END)
        self.ui.name_entry.insert(0, "Bulbasaur")
        self.ui.dex_entry.delete(0, tk.END)
        self.ui.dex_entry.insert(0, "1")
        self.ui.set_entry.delete(0, tk.END)
        self.ui.set_entry.insert(0, "Base Set")
        self.ui.date_entry.delete(0, tk.END)
        self.ui.date_entry.insert(0, "2023-13-01")
        
        self.ui.submit_card()
        mock_showerror.assert_called_with("Error", "Release Date must be a valid date.")
        self.assertEqual(len(self.card_repo.get_cards()), 0)

    def test_cancel(self):
        self.ui.name_entry.delete(0, tk.END)
        self.ui.name_entry.insert(0, "Bulbasaur")
        self.ui.cancel()
        self.assertEqual(self.ui.name_entry.get(), "Esim: Bulbasaur")
        self.assertEqual(self.ui.dex_entry.get(), "1 - 1025")
        self.assertEqual(self.ui.set_entry.get(), "Esim: Base Set")
        self.assertEqual(self.ui.date_entry.get(), "YYYY-MM-DD")
        self.assertEqual(self.ui.name_entry.cget("fg"), "grey")
        self.controller.show_frame.assert_called_with("HomePage")

if __name__ == "__main__":
    unittest.main()