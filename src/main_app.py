import tkinter as tk
from ui.home_page_view import HomePage
from ui.new_card_view import NewCard
from repositories.card_repository import CardRepository as cr

class MainApp:
    """Sovelluksen toiminnasta vastaava luokka.
    """

    def __init__(self, root):
        """Luokan konstruktori.
        
        Args:
            root: 
                Tkinter-ikkuna.
            container:
                Luo erillisen kehyksen.
            card_repo:
                Alustaa korttirepositorion.
            frames:
                Sisältää kaikki kehykset.
        """


        self.root = root
        self.root.title("Pokemon Card App")
        self.root.minsize(900, 600)

        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.card_repo = cr()

        self.frames = {}

        for f, cls in [('HomePage', HomePage), ('NewCard', NewCard)]:
            frame = cls(self.container, self, self.card_repo)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('HomePage')

    def show_frame(self, page):
        """Tuo uuden kehyksen / ikkunan esille.
        """


        for frame in self.frames.values():
            frame.grid_remove()

        frame = self.frames[page]
        frame.grid(row=0, column=0, sticky="nsew")
        if page == 'HomePage':
            frame.display_cards()
        frame.tkraise()

    def destroy(self):
        """Tuhoaa Tkinter-ikkunan ja sulkee tietokantayhteyden.
        """


        if hasattr(self, '_skip_conn_close') and self._skip_conn_close:
            pass
        else:
            self.card_repo.conn.close()
        self.card_repo.conn.close()
        self.root.destroy()
