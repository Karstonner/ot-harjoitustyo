from repositories.card_repository import card_repository as cr
import tkinter as tk
from tkinter import ttk


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Card App")
        self.root.minsize(900, 600)
        heading = tk.Label(self.root, text="Your cards")
        heading.grid(row=0, column=5, columnspan=2, pady=(10, 20), sticky="n")
        self.start()
    
    def start(self):
        self.add_button = tk.Button(self.root, text="Add card", fg="black", bg="white",
                                    command=self.show_add)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.add_frame = tk.Frame(self.root)
        self.setup_add_frame()
        self.add_frame.grid_remove()

        self.card_header_frame = tk.Frame(self.root)
        self.setup_card_headers()
        self.card_header_frame.grid_remove()

        self.display_cards()
    
    def setup_add_frame(self):
        tk.Label(self.add_frame, text="Pokemon's Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.add_frame)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.add_frame, text="Dex Number").grid(row=2, column=0)
        self.dex_entry = tk.Entry(self.add_frame)
        self.dex_entry.grid(row=2, column=1)

        tk.Label(self.add_frame, text="Card Set").grid(row=3, column=0)
        self.set_entry = tk.Entry(self.add_frame)
        self.set_entry.grid(row=3, column=1)

        tk.Label(self.add_frame, text="Release Date").grid(row=4, column=0)
        self.date_entry = tk.Entry(self.add_frame)
        self.date_entry.grid(row=4, column=1)

        submit_button = tk.Button(self.add_frame, text="Submit", command=self.add_new)
        submit_button.grid(row=5, column=0, pady=5)

        cancel_button = tk.Button(self.add_frame, text="Cancel", command=self.hide_add)
        cancel_button.grid(row=5, column=1, pady=5)
    
    def setup_card_headers(self):
        self.name_header = tk.Label(self.card_header_frame, text="Pokémon")
        self.name_header.grid(row=3, column=6, columnspan=1, padx=5, pady=5, sticky="n")

        self.dex_header = tk.Label(self.card_header_frame, text="Dex")
        self.dex_header.grid(row=3, column=7, columnspan=1, padx=5, pady=5, sticky="n")

        self.set_header = tk.Label(self.card_header_frame, text="Set")
        self.set_header.grid(row=3, column=8, columnspan=1, padx=5, pady=5, sticky="n")

        self.date_header = tk.Label(self.card_header_frame, text="Release Date")
        self.date_header.grid(row=3, column=9, columnspan=1, padx=5, pady=5, sticky="n")

    def add_new(self):
        name = self.name_entry.get()
        number = self.dex_entry.get()
        card_set = self.set_entry.get()
        release_date = self.date_entry.get()

        if name and number and card_set and release_date:
            cr.new_card(name, number, card_set, release_date)
            self.display_cards()
            self.hide_add()
        
    
    def display_cards(self):
        # I got inspiration for this from https://www.plus2net.com/python/tkinter-mysql.php
        i = 0
        cards = cr.get_cards()
        for card in cards:
            for j in range(1, len(card)):
                entry = tk.Label(window, text=card[j])
                entry.grid(row=4+i, column=5+j, columnspan=1, padx=10, pady=5, sticky="n")
            i += 1
        # Inspiration ends
        
        if cards:
            self.setup_card_headers()
            self.card_header_frame.grid(row=3, column=5, columnspan=4)
        else:
            self.card_header_frame.grid_remove()

    def show_add(self):
        self.add_button.grid_remove()
        self.add_frame.grid(row=1, column=0, columnspan=2, pady=10)
    
    def hide_add(self):
        self.add_frame.grid_remove()
        self.clear_fields()
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.dex_entry.delete(0, tk.END)
        self.set_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        
        

if __name__ == "__main__":
    window = tk.Tk()
    ui = UI(window)
    window.mainloop()
