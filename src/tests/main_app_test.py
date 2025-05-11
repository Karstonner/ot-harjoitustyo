import unittest
import tkinter as tk
from main_app import MainApp
from ui.home_page_view import HomePage
from ui.new_card_view import NewCard
from tests.test_db import get_test_connection
from initialize import initialize

class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.conn = get_test_connection()
        initialize(self.conn)
        self.root = tk.Tk()
        self.app = MainApp(self.root)
        self.app._skip_conn_close = True
        self.root.update()
    
    def tearDown(self):
        self.app.destroy()
        self.conn.close()

    def test_window_title(self):
        self.assertEqual(self.root.title(), "Pokemon Card App")
    
    def test_window_size(self):
        self.assertEqual(self.root.minsize(), (900, 600))
    
    def test_frame_initialization(self):
        self.assertIn("HomePage", self.app.frames)
        self.assertIn("NewCard", self.app.frames)
        self.assertIsInstance(self.app.frames["HomePage"], HomePage)
        self.assertIsInstance(self.app.frames["NewCard"], NewCard)

    def test_show_frame(self):
        self.app.show_frame("NewCard")
        self.root.update()
        self.assertTrue(self.app.frames["NewCard"].winfo_ismapped())
        self.assertFalse(self.app.frames["HomePage"].winfo_ismapped())
        self.app.show_frame("HomePage")
        self.root.update()
        self.assertTrue(self.app.frames["HomePage"].winfo_ismapped())
        self.assertFalse(self.app.frames["NewCard"].winfo_ismapped())


if __name__ == "__main__":
    unittest.main()