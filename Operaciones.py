from tkinter import*
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os
from io import open

from Ventana_Fuente import Ventana_Fuente

# Para almacenar el nombre del archivo actual
global nombre_archivo
nombre_archivo = ''

# Para saber si el archivo actual esta o no guardado
global archivo_guardado
archivo_guardado = False

# Para almacenar el contenido del widget Text
global auxiliar
auxiliar = False


############################################### Menu Archivo ######################################################
def nuevo_archivo(raiz, area_texto, evento):
    """Para crear un archivo nuevo."""

    global nombre_archivo, archivo_guardado
    nombre_archivo = ''
    archivo_guardado = False
    
    raiz.title('Sin_titulo - Notas\u00AE')
    # Elimina el archivo de texto previo
    area_texto.delete(1.0, END)


def abrir_archivo(raiz, area_texto, evento):
    """Para seleccionar un archivo de la pc."""

    global nombre_archivo, archivo_guardado, auxiliar
    archivo = fd.askopenfilename(defaultextension='.txt', filetypes=[('Documentos de texto', '*.txt*')])
    
    if archivo: #Si hay un nombre de archivo
        nombre_archivo = archivo
        raiz.title(f"{os.path.basename(archivo.split('/')[-1].split('.')[0])} - Notas\u00AE")
        # Borra el contenido del widget Text
        area_texto.delete(1.0, END)
        with open(archivo, 'r') as archivo_texto:
            area_texto.insert(1.0, archivo_texto.read())
            archivo_texto.close()

        archivo_guardado = True
        auxiliar = area_texto.get(1.0, END)

def guardar_archivo(raiz, area_texto, evento):
    """Para guardar el archivo de texto."""

    global nombre_archivo, archivo_guardado, auxiliar
    
    if nombre_archivo: #Si es distinto de vacio
        texto = area_texto.get(1.0, END)
        auxiliar = texto
        archivo = open(nombre_archivo, 'w')
        archivo.write(texto)
        archivo.close()
        archivo_guardado = True
    else:
        guardar_como_archivo(raiz, area_texto, evento)
    

def guardar_como_archivo(raiz, area_texto, evento):
    """Para guardar el archivo de texto."""

    global nombre_archivo, archivo_guardado, auxiliar
    archivo = fd.asksaveasfile(mode='w', 
            initialfile='Sin_titulo.txt', 
            defaultextension='.txt',
            filetypes=[('Documentos de texto', '*.txt*')])
    
    if archivo: #Si distinto de vacio
        texto = area_texto.get(1.0, END)
        auxiliar = texto
        archivo.write(texto)
        archivo.close()
        
        nombre_archivo = __get_nombre_archivo(archivo)
        raiz.title(f'{nombre_archivo} - Notas\u00AE')
        archivo_guardado = True


def salir(raiz, area_texto):
    """Para cerrar el programa."""

    if archivo_guardado and auxiliar != area_texto.get(1.0, END):
        if mb.askyesno('Guardar archivo', '¿Desea guardar los cambios?'):
            guardar_archivo(raiz, area_texto, False)
            raiz.destroy()
        else:
            raiz.destroy()
    elif archivo_guardado and auxiliar == area_texto.get(1.0, END):
        raiz.destroy()
    elif not archivo_guardado and area_texto.get(1.0, END) == '\n': # Si esta vacio. Por defecto Text tiene el caracter \n
        raiz.destroy()
    elif not archivo_guardado and area_texto.get(1.0, END) != '\n': # Si no esta vacio
        if mb.askyesno('Guardar archivo', '¿Desea guardar el archivo?'):
            guardar_archivo(raiz, area_texto, False)
            raiz.destroy()
        else:
            raiz.destroy()

def __get_nombre_archivo(archivo):
    """Retorna el nombre del archivo."""
    
    nombre_ruta, extension = os.path.splitext(archivo.name)
    nombre = nombre_ruta.split('/')
    return nombre[-1] #Ultimo elemento de la lista



############################################### Menu Editar ######################################################
def copiar_archivo(area_texto):
    """Para copiar una porción de texto."""

    area_texto.event_generate('<<Copy>>')


def cortar_archivo(area_texto):
    """Para cortar una porción de texto."""

    area_texto.event_generate('<<Cut>>')


def pegar_archivo(area_texto):
    """Para pegar la porción de texto que se copió o cortó."""

    area_texto.event_generate('<<Paste>>')


def seleccionar_todo_archivo(area_texto, evento):
    """Para seleccionar todo el contenido del texto."""

    area_texto.tag_add(SEL, '1.0', END)
    area_texto.mark_set(INSERT, '1.0')
    area_texto.see(INSERT)




############################################### Menu Formato ########################################################
def ajuste_de_linea(valor_ajuste, area_texto):
    """Para ajustar el texto al tamaño de la ventana."""
    if valor_ajuste.get():
        area_texto.config(wrap=CHAR)
    else:
        area_texto.config(wrap=NONE)


def modo_oscuro(valor_oscuro, area_texto):
    """Establece o quita el modo ocuro al widget Text."""
    
    if valor_oscuro.get():
        area_texto.config(background='gray17', 
            foreground='white', 
            insertbackground='#fff') #Color de cursor de texto
    else:
        area_texto.config(background='white', 
            foreground='black',
            insertbackground='black') #Color de cursor de texto


def fuente(area_texto):
    """Abre una ventana para configurar la fuente del widget Text."""
    
    Ventana_Fuente(area_texto)


############################################### Menu Ayuda ######################################################
def acerca_de():
    mensaje = '''
        Notas\u00AE v1.0

        Contactos:
        editor_simple@email.com
    '''
    mb.showinfo('Notas\u00AE', mensaje)