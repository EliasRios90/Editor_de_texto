import tkinter as tk

from Menubar import Menubar
from Editor import Editor
from Operaciones import salir

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sin_titulo - Notas\u00AE")
        self.iconbitmap("icono.ico")
        self.geometry("850x600+350+10")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        editor = Editor(self)
        editor.pack()
        Menubar(self, editor.get_area_texto())
        
        # Protocolo que define que pasa si el usuario cierra el programa utilizando el gestor de ventanas
        self.protocol("WM_DELETE_WINDOW", lambda: salir(self, editor.get_area_texto()))



if __name__=="__main__":
    app = App()
    app.mainloop()
