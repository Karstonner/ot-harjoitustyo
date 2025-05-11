import tkinter as tk
from main_app import MainApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.protocol("WM_DELETE_WINDOW", app.destroy)
    root.mainloop()
