import tkinter as tk
#import repositories.card_repository as cr
from repositories.card_repository import CardRepository as cr

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Card App")
        self.root.minsize(900, 600)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.sort_by = None
        self.sort_ascending = True
        self.header_labels = []
        self.card_widgets = []
        self.cr = cr()
        self.setup()

    def setup(self):
        heading = tk.Label(self.root, text="Your cards")
        heading.grid(row=0, column=1, columnspan=2, sticky="n")
        self.add_button = tk.Button(self.root, text="Add card", fg="black", bg="white",
                                    command=self.show_add)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.add_frame = tk.Frame(self.root)
        self.card_header_frame = tk.Frame(self.root)

        self.name_entry = tk.Entry(self.add_frame)
        self.name_header = tk.Label(self.card_header_frame, text="Pokémon")
        self.dex_entry = tk.Entry(self.add_frame)
        self.dex_header = tk.Label(self.card_header_frame, text="Dex")
        self.set_entry = tk.Entry(self.add_frame)
        self.set_header = tk.Label(self.card_header_frame, text="Set")
        self.date_entry = tk.Entry(self.add_frame)
        self.date_header = tk.Label(self.card_header_frame, text="Release Date")

        self.setup_add_frame()
        self.add_frame.grid_remove()
        self.setup_card_headers()
        self.card_header_frame.grid_remove()
        self.display_cards()

    def setup_add_frame(self):
        tk.Label(self.add_frame, text="Pokemon's Name").grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.add_frame, text="Dex Number").grid(row=2, column=0)
        self.dex_entry.grid(row=2, column=1)

        tk.Label(self.add_frame, text="Card Set").grid(row=3, column=0)
        self.set_entry.grid(row=3, column=1)

        tk.Label(self.add_frame, text="Release Date").grid(row=4, column=0)
        self.date_entry.grid(row=4, column=1)

        submit_button = tk.Button(self.add_frame, text="Submit", command=self.add_new)
        submit_button.grid(row=5, column=0, pady=5)

        cancel_button = tk.Button(self.add_frame, text="Cancel", command=self.hide_add)
        cancel_button.grid(row=5, column=1, pady=5)

    def setup_card_headers(self):
        headers = ["Pokémon", "Dex #", "Expansion", "Release Date"]
        self.header_labels = []

        for col, header in enumerate(headers, start=4):
            label = tk.Label(self.card_header_frame, text=header)
            label.grid(row=3, column=col+1, padx=5, pady=5)
            label.bind("<Button-1>", lambda x, idx=col-4: self.setup_sorting(idx))
            self.header_labels.append(label)

        for col in range(5, 9):
            self.card_header_frame.columnconfigure(col, weight=1)

    def show_add(self):
        self.add_button.grid_remove()
        self.add_frame.grid(row=1, column=0, columnspan=2, pady=10)

    def hide_add(self):
        self.add_frame.grid_remove()
        self.clear_fields()
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def display_cards(self):
        for row in getattr(self, "card_widgets", []):
            for widget in row:
                widget.destroy()
        self.card_widgets = []

        self.card_header_frame.grid_remove()
        cards = self.cr.get_cards()

        if self.sort_by is not None:
            index = self.sort_by
            cards.sort(key=lambda x: x[index], reverse=not self.sort_ascending)

        i = 0
        for card in cards:
            row_widgets = []

            entry_poke = tk.Label(self.card_header_frame, text=card[0])
            entry_poke.grid(row=5+i, column=5, columnspan=1, padx=5, pady=5)
            row_widgets.append(entry_poke)

            entry_dex = tk.Label(self.card_header_frame, text=card[1])
            entry_dex.grid(row=5+i, column=6, columnspan=1, padx=5, pady=5)
            row_widgets.append(entry_dex)

            entry_set = tk.Label(self.card_header_frame, text=card[2])
            entry_set.grid(row=5+i, column=7, columnspan=1, padx=5, pady=5)
            row_widgets.append(entry_set)

            entry_date = tk.Label(self.card_header_frame, text=card[3])
            entry_date.grid(row=5+i, column=8, columnspan=1, padx=5, pady=5)
            row_widgets.append(entry_date)

            remove_button = tk.Button(self.card_header_frame, text="Remove",
                                      command=lambda c=card, w=row_widgets: self.remove_card(c, w))
            remove_button.grid(row=5+i, column=9, columnspan=1, padx=5, pady=5)
            row_widgets.append(remove_button)

            self.card_widgets.append(row_widgets)

            i += 1

        if len(cards) == 1:
            amount = tk.Label(self.root, text=" 1 card owned")
            amount.grid(row=1, column=10, columnspan=2, padx=10, sticky="e")
        else:
            amount = tk.Label(self.root, text=f" {len(cards)} cards owned")
            amount.grid(row=1, column=10, columnspan=2, padx=10, sticky="e")

        if len(cards) > 0:
            self.setup_card_headers()
            self.card_header_frame.grid(row=4, column=5, columnspan=5)
        else:
            self.card_header_frame.grid_remove()

    def setup_sorting(self, sort_index):
        if self.sort_by == sort_index:
            self.sort_ascending = not self.sort_ascending
        else:
            self.sort_by = sort_index
            self.sort_ascending = True
        self.display_cards()

    @staticmethod
    def sort_cards(cards, sort_by, ascending):
        return sorted(cards, key=lambda x: x[sort_by], reverse=not ascending)

    def add_new(self):
        name = self.name_entry.get()
        number = self.dex_entry.get()
        card_set = self.set_entry.get()
        release_date = self.date_entry.get()

        if name and number and card_set and release_date:
            self.cr.new_card(name, number, card_set, release_date)
            self.display_cards()
            self.hide_add()

    def remove_card(self, card, widgets):
        self.cr.remove_card(card[0], card[1], card[2], card[3])
        for widget in widgets:
            widget.destroy()
        self.display_cards()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.dex_entry.delete(0, tk.END)
        self.set_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
