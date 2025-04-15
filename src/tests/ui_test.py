import unittest
import tkinter as tk
from gui import UI
from initialize import initialize


class TestIndex(unittest.TestCase):
    def setUp(self):
        initialize()
        self.root = tk.Tk()
        self.ui = UI(self.root)

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