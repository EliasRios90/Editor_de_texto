from tkinter import*


class Editor(Frame):
    def __init__(self, raiz):
        super().__init__(raiz)

        vertical_scrollbar = Scrollbar(raiz, orient=VERTICAL)
        vertical_scrollbar.pack( side = RIGHT, fill = Y )
        
        horizontal_scrollbar = Scrollbar(raiz, orient=HORIZONTAL)
        horizontal_scrollbar.pack( side = BOTTOM, fill = X )

        self.area_texto = Text(raiz, 
            font=('Times New Roman', 12, 'normal'), 
            padx=10,
            pady=10,
            undo=True,
            wrap=NONE,
            yscrollcommand=vertical_scrollbar.set, 
            xscrollcommand=horizontal_scrollbar.set)
        self.area_texto.pack(side=TOP, fill=BOTH, expand=True)
        
        vertical_scrollbar.config( command = self.area_texto.yview )
        horizontal_scrollbar.config( command = self.area_texto.xview )
    

    def get_area_texto(self):
        return self.area_texto    
    