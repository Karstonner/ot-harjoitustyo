import tkinter as tk
from tkinter import messagebox as mb
from repositories.card_repository import CardRepository as cr

class HomePage(tk.Frame):
    """Sovelluksen avattua tämä sivu on näkyvissä.

    Attributes:
        parent: Tkinter-ikkuna, jota käsitellään.
        controller: näkymän vaihtava ohjain.
        card_repo: käsiteltävä korttirepositorio.
    """

    def __init__(self, parent, controller, card_repo):
        """Luokan konstruktori. Alustaa kaikki sivun elementit.
        
        Args:
            parent:
                Tkinter-ikkuna, johon näkymä luodaan.
            controller:
                Ohjain, joka mahdollistaa näkymän vaihtamisen.
            cr:
                Käsiteltävissä oleva korttirepositorio.
            sort_by:
                Järjestämisen määrittely, oletukselta None.
            sort_ascending:
                Boolean-arvo, järjestäminen joko nouseva tai laskeva.
            header_labels:
                Pitää listaa korttien otsikoista.
            card_widgets:
                Pitää listaa korteista riveittäin, pala palalta.
        """


        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.sort_by = None
        self.sort_ascending = True
        self.header_labels = []
        self.card_widgets = []
        self.cr = card_repo
        self.setup()

    def setup(self):
        """Asettaa otsikot ja alustaa kortin lisäämisen.
        """


        wrapper = tk.Frame(self)
        wrapper.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        wrapper.rowconfigure(1, weight=1)
        wrapper.columnconfigure(0, weight=1)
        wrapper.columnconfigure(1, weight=1)

        heading = tk.Label(wrapper, text="Your cards", font=("Arial", 16))
        heading.grid(row=0, column=0, columnspan=2, sticky="n", pady=(0, 10))

        self.add_button = tk.Button(wrapper, text="Add card", fg="black", bg="white",
                                    command=lambda: self.controller.show_frame('NewCard'))
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.card_header_frame = tk.Frame(self)
        self.setup_card_headers()
        self.card_header_frame.grid_remove()
        self.display_cards()

    def setup_card_headers(self):
        """Luo korteille otsikot niiden määrän mukaan.
        """


        headers = ["Pokémon", "Dex #", "Expansion", "Release Date"]
        self.header_labels = []

        for col, header in enumerate(headers):
            label = tk.Label(self.card_header_frame, text=header, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5, sticky="w")
            label.bind("<Button-1>", lambda x, idx=col: self.setup_sorting(idx))
            self.header_labels.append(label)

        for col in range(4):
            self.card_header_frame.columnconfigure(col, weight=1)

    def display_cards(self):
        """Tuo kaikki olemassa olevat kortit näkyviin.
        """


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

            entry_poke = tk.Label(self.card_header_frame, text=card.pokemon)
            entry_poke.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
            row_widgets.append(entry_poke)

            entry_dex = tk.Label(self.card_header_frame, text=card.pokedex_number)
            entry_dex.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
            row_widgets.append(entry_dex)

            entry_set = tk.Label(self.card_header_frame, text=card.expansion)
            entry_set.grid(row=i+1, column=2, padx=10, pady=5, sticky="w")
            row_widgets.append(entry_set)

            entry_date = tk.Label(self.card_header_frame, text=card.release_date)
            entry_date.grid(row=i+1, column=3, padx=10, pady=5, sticky="w")
            row_widgets.append(entry_date)

            remove_button = tk.Button(self.card_header_frame, text="Remove",
                                      command=lambda c=card, w=row_widgets: self.remove_card(c, w))
            remove_button.grid(row=i+1, column=4, padx=10, pady=5)
            row_widgets.append(remove_button)

            self.card_widgets.append(row_widgets)

            i += 1

        card_count = len(cards)
        amount_text = " 1 card owned" if card_count == 1 else f"{card_count} cards owned"

        if card_count > 0:
            self.setup_card_headers()
            self.card_header_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        else:
            self.card_header_frame.grid_remove()
        
        amount = tk.Label(self.card_header_frame, text=amount_text, font=("Arial", 12))
        amount.grid(row=0, column=0, columnspan=5, pady=(10, 0), sticky="e")
    
    def _get_sort_key(self, card, index):
        """Helper method to get the sort key for a Card object.
        """


        if index == 0:
            return card.pokemon
        elif index == 1:
            return card.pokedex_number
        elif index == 2:
            return card.expansion
        elif index == 3:
            return card.release_date
        return ""

    def setup_sorting(self, sort_index):
        """Asettaa korttien järjestyksen halujen mukaiseksi.
        """


        if self.sort_by == sort_index:
            self.sort_ascending = not self.sort_ascending
        else:
            self.sort_by = sort_index
            self.sort_ascending = True
        self.display_cards()

    @staticmethod
    def sort_cards(cards, sort_by, ascending):
        """Staattinen metodi, joka järjestää kortit klikkauksella.
        """


        return sorted(cards, key=lambda x: x[sort_by], reverse=not ascending)

    def remove_card(self, card, widgets):
        """Poistaa kortin tietokannasta ja repositoriosta.
        """

        
        confirmation = mb.askquestion("Remove Card", "Are you sure you want to remove this card?")
        if confirmation == "yes":    
            self.cr.remove_card(card.pokemon, card.pokedex_number, card.expansion, card.release_date)
            for widget in widgets:
                widget.destroy()
            self.display_cards()