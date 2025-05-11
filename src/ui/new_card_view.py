import tkinter as tk
from tkinter import messagebox as mb
from repositories.card_repository import CardRepository
from entities.card import Card

class NewCard(tk.Frame):
    """Kortin lisäämisen näkymä.

    Attributes:
        parent: Tkinter-ikkuna, jota käsitellään.
        controller: näkymän vaihtava ohjain.
        card_repo: käsiteltävä korttirepositorio.
    """

    def __init__(self, parent, controller, card_repo):
        """Luokan konstruktori.
        
        Args:
            parent:
                Tkinter-ikkuna, johon näkymä luodaan.
            controller:
                Ohjain, joka mahdollistaa näkymän vaihtamisen.
            card_repo:
                Käsiteltävissä oleva korttirepositorio.
        """


        super().__init__(parent)
        self.controller = controller
        self.card_repo = card_repo
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.create_form()

    def create_form(self):
        """Luo tekstikentät, joiden perusteella uusi kortti tehdään.
        """


        form_frame = tk.Frame(self)
        form_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=2)

        self.name_entry = tk.Entry(form_frame, width=30)
        self.dex_entry = tk.Entry(form_frame, width=30)
        self.set_entry = tk.Entry(form_frame, width=30)
        self.date_entry = tk.Entry(form_frame, width=30)

        self.name_entry.insert(0, "Esim: Bulbasaur")
        self.name_entry.config(fg="grey")
        self.name_entry.bind("<FocusIn>", self.name_focus_in)

        self.dex_entry.insert(0, "1 - 1025")
        self.dex_entry.config(fg="grey")
        self.dex_entry.bind("<FocusIn>", self.dex_focus_in)

        self.set_entry.insert(0, "Esim: Base Set")
        self.set_entry.config(fg="grey")
        self.set_entry.bind("<FocusIn>", self.set_focus_in)

        self.date_entry.insert(0, "YYYY-MM-DD")
        self.date_entry.config(fg="grey")
        self.date_entry.bind("<FocusIn>", self.date_focus_in)

        tk.Label(form_frame, text="Pokemon's Name:", anchor="e").grid(
                        row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Dex Number:", anchor="e").grid(
                    row=2, column=0, padx=5, pady=5, sticky="e")
        self.dex_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Card Set:", anchor="e").grid(
                    row=3, column=0, padx=5, pady=5, sticky="e")
        self.set_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Release Date:", anchor="e").grid(
                    row=4, column=0, padx=5, pady=5, sticky="e")
        self.date_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        submit_button = tk.Button(form_frame, text="Submit", command=self.submit_card)
        submit_button.grid(row=5, column=0, padx=5, pady=10)

        cancel_button = tk.Button(form_frame, text="Cancel", command=self.cancel)
        cancel_button.grid(row=5, column=1, padx=5, pady=10, sticky="w")
    
    # Inspiraatio seuraaviin focus_in-komentoihin täältä: 
    # https://stackoverflow.com/questions/51781651/showing-a-greyed-out-default-text-in-a-tk-entry
    
    def name_focus_in(self, _):
        """Poistaa oletustekstin nimikentästä.
        """


        self.name_entry.delete(0, tk.END)
        self.name_entry.config(fg="black")
    
    def dex_focus_in(self, _):
        """Poistaa oletustekstin pokedex-kentästä.
        """


        self.dex_entry.delete(0, tk.END)
        self.dex_entry.config(fg="black")
    
    def set_focus_in(self, _):
        """Poistaa oletustekstin settikentästä.
        """


        self.set_entry.delete(0, tk.END)
        self.set_entry.config(fg="black")
    
    def date_focus_in(self, _):
        """Poistaa oletustekstin päivämääräkentästä.
        """


        self.date_entry.delete(0, tk.END)
        self.date_entry.config(fg="black")
    
    def submit_card(self):
        """Luo uuden kortin.
        """


        name = self.name_entry.get()
        number = self.dex_entry.get()
        card_set = self.set_entry.get()
        release_date = self.date_entry.get()

        placeholders = {
            "Esim: Bulbasaur": "",
            "1 - 1025": "",
            "Esim: Base Set": "",
            "YYYY-MM-DD": ""
        }
        name = placeholders.get(name, name)
        number = placeholders.get(number, number)
        card_set = placeholders.get(card_set, card_set)
        release_date = placeholders.get(release_date, release_date)

        if not (name and number and card_set and release_date):
            mb.showerror("Error", "All fields are required.")
            return
        
        try:
            pokedex_number = int(number)
            if not 1 <= pokedex_number <= 1025:
                mb.showerror("Error", "Dex Number must be between 1 and 1025.")
                return
        except ValueError:
            mb.showerror("Error", "Dex Number must be a valid integer.")
            return
        
        import re
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", release_date):
            mb.showerror("Error", "Release Date must be in YYYY-MM-DD format.")
            return
        try:
            from datetime import datetime
            datetime.strptime(release_date, "%Y-%m-%d")
        except ValueError:
            mb.showerror("Error", "Release Date must be a valid date.")
            return
        
        try:
            self.card_repo.new_card(name, pokedex_number, card_set, release_date)
            self.clear_fields()
            self.controller.show_frame('HomePage')
        except Exception as e:
            mb.showerror("Error", f"Failed to add card: {str(e)}")

    def cancel(self):
        """Peruuttaa kortin luonnin.
        """


        self.clear_fields()
        self.controller.show_frame('HomePage')

    def clear_fields(self):
        """Tyhjentää tekstikentät.
        """

        
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Esim: Bulbasaur")
        self.name_entry.config(fg="grey")

        self.dex_entry.delete(0, tk.END)
        self.dex_entry.insert(0, "1 - 1025")
        self.dex_entry.config(fg="grey")

        self.set_entry.delete(0, tk.END)
        self.set_entry.insert(0, "Esim: Base Set")
        self.set_entry.config(fg="grey")

        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, "YYYY-MM-DD")
        self.date_entry.config(fg="grey")