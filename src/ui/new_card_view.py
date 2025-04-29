import tkinter as tk
from ui.home_page_view import HomePage
from repositories.card_repository import CardRepository as cr

class NewCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Add a New Card")
        self.root.minsize(900, 600)
        self.frame = tk.Frame(self.root)

    def new_card(self):
        self.name_entry = tk.Entry(self.frame)
        self.dex_entry = tk.Entry(self.frame)
        self.set_entry = tk.Entry(self.frame)
        self.date_entry = tk.Entry(self.frame)
        submit_button  = tk.Button(self.frame, text="Submit", command=self.submit_card)

        tk.Label(self.frame, text="Pokemon's Name").grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Dex Number").grid(row=2, column=0)
        self.dex_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Card Set").grid(row=3, column=0)
        self.set_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Release Date").grid(row=4, column=0)
        self.date_entry.grid(row=4, column=1)

        submit_button.grid(row=5, column=1, pady=5)

        self.clear_fields()
        self.frame.destroy()
        self.redirect()
    
    def submit_card(self):
        name = self.name_entry.get()
        number = self.dex_entry.get()
        card_set = self.set_entry.get()
        release_date = self.date_entry.get()

        if name and number and card_set and release_date:
            HomePage(self.root).card_repo(name, number, card_set, release_date)

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.dex_entry.delete(0, tk.END)
        self.set_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
    
    def redirect(self):
        self.frame.destroy()
        HomePage(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewCard(root)
    root.mainloop()