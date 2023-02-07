from tkinter import*
from tkinter import font
from tkinter import ttk

class Ventana_Fuente(Toplevel):
    def __init__(self, area_texto):
        super().__init__()
        self.title('Fuente - Notas\u00AE')
        self.iconbitmap("icono.ico")
        self.geometry('600x450')
        self.area_texto = area_texto

        self.set_fuente(area_texto)
        self.uEstilo = 'normal'
        self.set_tamanio(area_texto)

        ###############################################################################################
        ############################## FRAME PARA LA SELECCION DE LA FUENTE ###########################
        frame_fuente = Frame(self)
        frame_fuente.grid(row=0, column=0, padx=20)

        Label(frame_fuente, text='Fuente:').pack()
        self.fuente_entry = Entry(frame_fuente,
            font=('Helvetica', 9),
            width=32,
            bd=3,
            relief=SUNKEN,
            background='lightgray')
        self.fuente_entry.insert(END, self.uFuente)
        self.fuente_entry.pack()

        self.lista_fuentes = Listbox(frame_fuente,
            height=10,
            width=30,
            font=('Helvetica', 9))
        self.lista_fuentes.pack(side=LEFT)
        for f in font.families():
            self.lista_fuentes.insert(END, f)
        
        scrollbar_fuentes = Scrollbar(frame_fuente, orient=VERTICAL)
        scrollbar_fuentes.pack(side=RIGHT, fill=Y)
        scrollbar_fuentes.config(command=self.lista_fuentes.yview)
        self.lista_fuentes.config(yscrollcommand=scrollbar_fuentes.set)

        self.lista_fuentes.bind('<ButtonRelease-1>', self.fuente_seleccion)

        ###############################################################################################
        ############################## FRAME PARA LA SELECCION DE ESTILO ##############################
        frame_estilo = Frame(self)
        frame_estilo.grid(row=0, column=1, padx=30)

        Label(frame_estilo, text='Estilo de fuente:').pack()
        self.estilo_entry = Entry(frame_estilo,
            font=('Helvetica', 9),
            width=20,
            bd=3,
            relief=SUNKEN,
            background='lightgray')
        self.estilo_entry.insert(END, self.get_estilo_entry(area_texto))
        self.estilo_entry.pack()

        self.estilo_fuente = Listbox(frame_estilo,
            height=10,
            width=20,
            font=('Helvetica', 9))
        self.estilo_fuente.insert(END, 'Normal')
        self.estilo_fuente.insert(END, 'Cursiva')
        self.estilo_fuente.insert(END, 'Negrita')
        self.estilo_fuente.insert(END, 'Negrita y cursiva')
        self.estilo_fuente.pack(side=LEFT)

        self.estilo_fuente.bind('<ButtonRelease-1>', self.estilo_seleccion)

        ##############################################################################################
        ############################## FRAME PARA LA SELECCION DE TAMAÑO #############################
        frame_tamanio = Frame(self)
        frame_tamanio.grid(row=0, column=2, padx=20)

        Label(frame_tamanio, text='Tamaño:').pack()
        self.tamanio_entry = Entry(frame_tamanio,
            font=('Helvetica', 9),
            width=11,
            bd=3,
            relief=SUNKEN,
            background='lightgray')
        self.tamanio_entry.insert(END, self.uTamanio)
        self.tamanio_entry.pack()

        self.tamanio_fuente = Listbox(frame_tamanio,
            height=10,
            width=9,
            font=('Helvetica', 10))
        self.tamanio_fuente.pack(side=LEFT)
        for i in range(8, 29):
            if i<=12:
                self.tamanio_fuente.insert(END, i)
            if i>=12 and i<=27 and i%2==0:
                self.tamanio_fuente.insert(END, i+2)
        self.tamanio_fuente.insert(END, 36)
        self.tamanio_fuente.insert(END, 48)
        self.tamanio_fuente.insert(END, 72)

        scrollbar_tamanio = Scrollbar(frame_tamanio, orient=VERTICAL)
        scrollbar_tamanio.pack(side=RIGHT, fill=Y)
        scrollbar_tamanio.config(command=self.tamanio_fuente.yview)
        self.tamanio_fuente.config(yscrollcommand=scrollbar_tamanio.set)

        self.tamanio_fuente.bind('<ButtonRelease-1>', self.tamanio_seleccion)
        
        ##############################################################################################
        ############################# FRAME PARA MOSTRAR EL RESULTADO ################################
        frame_ejemplo = Frame(self)
        frame_ejemplo.grid(row=1, column=0, columnspan=3, pady=(10, 20))
        
        frame = ttk.Labelframe(frame_ejemplo, text='Ejemplo:', height=150, width=585)
        frame.pack_propagate(False) #Evita que el Labelframe se expanda al cambiar de tamaño self.fuente_usuario
        frame.pack()
        self.fuente_usuario = Label(frame, 
            text='AaBbYyZz', 
            justify=CENTER, 
            font=(self.uFuente, self.uTamanio, self.uEstilo))
        self.fuente_usuario.pack()

        ##############################################################################################
        ################################# FRAME PARA LOS BOTONES #####################################
        frame_botones = Frame(self)
        frame_botones.grid(row=2, column=0, columnspan=3)

        Button(frame_botones, 
            text='Aceptar', 
            background='blue', 
            foreground='white', 
            activebackground='white',
            activeforeground='blue',
            font=('Courier', 12, 'bold'), 
            command=self.aceptar).pack(side=LEFT, padx=30)
        Button(frame_botones, 
            text='Cancelar', 
            background='red', 
            foreground='white',
            activebackground='white',
            activeforeground='red', 
            font=('Courier', 12, 'bold'), 
            command=self.cancelar).pack(side=LEFT, padx=30)
    
##################################################################################################################
##################################################################################################################
##################################################################################################################
    def fuente_seleccion(self, evento):
        """Para mostrar la selección del tipo de fuente."""

        self.fuente_entry.delete(0, END)
        self.uFuente = self.lista_fuentes.get(self.lista_fuentes.curselection())
        self.fuente_entry.insert(END, self.lista_fuentes.get(self.lista_fuentes.curselection()))
        self.fuente_usuario.config(font=(self.uFuente, self.uTamanio, self.uEstilo))
    

    def estilo_seleccion(self, evento):
        """Para mostrar la selección del estilo de fuente."""

        if self.estilo_fuente.get(self.estilo_fuente.curselection())=='Negrita':
            self.uEstilo = 'bold'
        elif self.estilo_fuente.get(self.estilo_fuente.curselection())=='Cursiva':
            self.uEstilo = 'italic'
        elif self.estilo_fuente.get(self.estilo_fuente.curselection())=='Negrita y cursiva':
            self.uEstilo = 'bold italic'
        else:
            self.uEstilo = 'normal'
        self.estilo_entry.delete(0, END)
        self.estilo_entry.insert(END, self.estilo_fuente.get(self.estilo_fuente.curselection()))
        self.fuente_usuario.config(font=(self.uFuente, self.uTamanio, self.uEstilo))
    

    def tamanio_seleccion(self, evento):
        """Para mostrar la selección del tamaño de fuente."""

        self.tamanio_entry.delete(0, END)
        self.uTamanio = self.tamanio_fuente.get(self.tamanio_fuente.curselection())
        self.tamanio_entry.insert(END, self.tamanio_fuente.get(self.tamanio_fuente.curselection()))
        self.fuente_usuario.config(font=(self.uFuente, self.uTamanio, self.uEstilo))



    def set_fuente(self, area_texto):
        """Asigna valor del tipo de fuente del widget Text a self.uFuente."""
        auxiliar = area_texto['font'].split(' ')
        if area_texto['font'][0]!='{' and 'bold italic' in area_texto['font']:
            self.uFuente = auxiliar[0]
        elif area_texto['font'][0] == '{' and 'bold italic' not in area_texto['font']:
            self.uFuente = area_texto['font'][1:area_texto['font'].index('}')]
        elif area_texto['font'][0]!='{' and 'bold italic' not in area_texto['font']:
            self.uFuente = auxiliar[0]
        elif area_texto['font'][0]=='{' and 'bold italic' in area_texto['font']:
            self.uFuente = area_texto['font'][1:area_texto['font'].index('}')]
        else:
            self.uFuente = 'ERROR'
        
    def get_estilo_entry(self, area_texto):
        """Retorna el estilo de fuente del widget Text."""

        if 'bold italic' in area_texto['font']:
            return 'Negrita y cursiva'
        else:
            if 'bold' in area_texto['font'] and 'normal' not in area_texto['font']:
                return 'Negrita'
            elif 'italic' in area_texto['font'] and 'normal' not in area_texto['font']:
                return 'Cursiva'
            else:
                return 'Normal'
    
    def set_tamanio(self, area_texto):
        """Asigna el valor del tamaño de fuente del widget Text a self.uTamanio."""
        
        auxiliar = ''
        for i in area_texto['font']:
            if i.isdigit():
                auxiliar += i
        self.uTamanio = int(auxiliar)




    def aceptar(self):
        """Asigna las configuraciones seleccionadas al widget Text."""
        
        self.area_texto.config(font=(self.uFuente, self.uTamanio, self.uEstilo))
        self.destroy()
    

    def cancelar(self):
        """Cancela la configuración y cierra la ventana."""
        
        self.destroy()
