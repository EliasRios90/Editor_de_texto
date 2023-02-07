from tkinter import*

from Operaciones import*


class Menubar:
    def __init__(self, raiz, area_texto):

        barra_menu = Menu(raiz)
        raiz.config(menu=barra_menu)

        
        menu_archivo = Menu(barra_menu, 
            tearoff=0,
            background='#e74166',
            foreground='white',
            activebackground='white',
            activeforeground='#e74166',
            font=('Tahoma', 8, 'bold'))
        #Agrego items a menu_archivo
        menu_archivo.add_command(label='Nuevo', command=lambda: nuevo_archivo(raiz, area_texto, False),accelerator='(Ctrl+N)')
        menu_archivo.add_command(label='Abrir...', command=lambda: abrir_archivo(raiz, area_texto, False),accelerator='(Ctrl+O)')
        menu_archivo.add_command(label='Guardar', command=lambda: guardar_archivo(raiz, area_texto, False),accelerator='(Ctrl+S)')
        menu_archivo.add_command(label='Guardar como...', command=lambda: guardar_como_archivo(raiz, area_texto, False),accelerator='(Ctrl+H)')
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=lambda: salir(raiz, area_texto))

        
        
        menu_editar = Menu(barra_menu,
            tearoff=0,
            background='#e74166',
            foreground='white',
            activebackground='white',
            activeforeground='#e74166',
            font=('Tahoma', 8, 'bold'))
        #Agrego items a menu_editar
        menu_editar.add_command(label='Deshacer', command=area_texto.edit_undo, accelerator='(Ctrl+Z)')
        menu_editar.add_command(label='Rehacer', command=area_texto.edit_redo, accelerator='(Ctrl+Y)')
        menu_editar.add_separator()
        menu_editar.add_command(label='Cortar', command=lambda: cortar_archivo(area_texto), accelerator='(Ctrl+X')
        menu_editar.add_command(label='Copiar', command=lambda: copiar_archivo(area_texto), accelerator='(Ctrl+C')
        menu_editar.add_command(label='Pegar', command=lambda: pegar_archivo(area_texto), accelerator='(Ctrl+V')
        menu_editar.add_separator()
        menu_editar.add_command(label='Seleccionar todo', command=lambda: seleccionar_todo_archivo(area_texto), accelerator='(Ctrl+A)')


        
        menu_formato = Menu(barra_menu,
            tearoff=0,
            background='#e74166',
            foreground='white',
            activebackground='white',
            activeforeground='#e74166',
            font=('Tahoma', 8, 'bold'))
        #Agrego items a menu_formato
        valor_ajuste = BooleanVar()
        valor_ajuste.set(False)
        # Opcion 'selectcolor' para cambiar el color del selector (palometa, tilde)
        menu_formato.add_checkbutton(label='Ajueste de línea', 
            selectcolor='white', 
            onvalue=1, 
            offvalue=0, 
            variable=valor_ajuste, 
            command=lambda: ajuste_de_linea(valor_ajuste, area_texto))
        valor_oscuro = BooleanVar()
        valor_oscuro.set(False)
        # Opcion 'selectcolor' para cambiar el color del selector (palometa, tilde)
        menu_formato.add_checkbutton(label='Modo oscuro', 
            selectcolor='white', 
            onvalue=1, 
            offvalue=0, 
            variable=valor_oscuro, 
            command=lambda: modo_oscuro(valor_oscuro, area_texto))
        menu_formato.add_command(label='Fuente...', command=lambda:fuente(area_texto))


        
        menu_ayuda = Menu(barra_menu,
            tearoff=0,
            background='#e74166',
            foreground='white',
            activebackground='white',
            activeforeground='#e74166',
            font=('Tahoma', 8, 'bold'))
        #Agrego items a menu_ayuda
        #menu_ayuda.add_command(label='Buscar actualizaciones', command=None)
        menu_ayuda.add_command(label='Acerca de ...', command=acerca_de)



        #Agrego los menues a la barra de menu
        barra_menu.add_cascade(label='Archivo', menu=menu_archivo)
        barra_menu.add_cascade(label='Editar', menu=menu_editar)
        barra_menu.add_cascade(label='Formato', menu=menu_formato)
        barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)


        #####################################################################################################
        #####################################################################################################
        #####################################################################################################
        # Eventos de teclado
        # lambda _: para evitar error TypeError: <lambda>() takes 0 positional arguments but 1 was given
        # Archivo
        raiz.bind('<Control-Key-n>', lambda _: nuevo_archivo(raiz, area_texto, False))
        raiz.bind('<Control-Key-o>', lambda _: abrir_archivo(raiz, area_texto, False))
        raiz.bind('<Control-Key-s>', lambda _: guardar_archivo(raiz, area_texto, False))
        raiz.bind('<Control-Key-h>', lambda _: guardar_como_archivo(raiz, area_texto, False))