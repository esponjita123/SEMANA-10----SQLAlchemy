import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from crud.crud_operations import CRUDOperations
import os

# Eliminar el archivo de la base de datos si existe
if os.path.exists('articles.db'):
    os.remove('articles.db')

# Configuración de la base de datos para persistencia
engine = create_engine('sqlite:///articles.db')  # Guardado en archivo
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
crud = CRUDOperations(session)


# Función para crear un nuevo artículo
def crear_articulo():
    titulo = entrada_titulo.get()
    if titulo:
        articulo = crud.create_article(titulo)  # Almacena el objeto artículo creado
        messagebox.showinfo("Éxito", f"Artículo '{titulo}' creado.")

        # Guardar en el archivo de texto
        guardar_en_archivo(f"Artículo creado: ID={articulo.id}, Título='{titulo}'\n")

        entrada_titulo.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "El título no puede estar vacío.")


# Función para agregar un comentario a un artículo
def agregar_comentario():
    articulo_id = entrada_articulo_id.get()
    comentario = entrada_comentario.get()

    articulo = crud.read_article(int(articulo_id))
    if articulo:
        crud.create_comment(comentario, articulo)  # Crea el comentario
        messagebox.showinfo("Éxito", f"Comentario agregado al artículo {articulo.titulo}.")

        # Guardar en el archivo de texto
        guardar_en_archivo(f"Comentario agregado: Artículo ID={articulo.id}, Comentario='{comentario}'\n")

        entrada_articulo_id.delete(0, tk.END)
        entrada_comentario.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Artículo no encontrado.")


# Función para guardar información en un archivo de texto
def guardar_en_archivo(contenido):
    ruta_archivo = os.path.join(os.getcwd(), "articulos_y_comentarios.txt")
    with open(ruta_archivo, 'a') as archivo:
        archivo.write(contenido)


# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Artículos y Comentarios")

# Crear interfaz de artículos
tk.Label(ventana, text="Crear un nuevo artículo").grid(row=0, column=0, padx=10, pady=10)

tk.Label(ventana, text="Título del artículo:").grid(row=1, column=0, padx=10, pady=10)
entrada_titulo = tk.Entry(ventana)
entrada_titulo.grid(row=1, column=1, padx=10, pady=10)

boton_crear_articulo = tk.Button(ventana, text="Crear Artículo", command=crear_articulo)
boton_crear_articulo.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Crear interfaz de comentarios
tk.Label(ventana, text="Agregar un comentario").grid(row=3, column=0, padx=10, pady=10)

tk.Label(ventana, text="ID del artículo:").grid(row=4, column=0, padx=10, pady=10)
entrada_articulo_id = tk.Entry(ventana)
entrada_articulo_id.grid(row=4, column=1, padx=10, pady=10)

tk.Label(ventana, text="Comentario:").grid(row=5, column=0, padx=10, pady=10)
entrada_comentario = tk.Entry(ventana)
entrada_comentario.grid(row=5, column=1, padx=10, pady=10)

boton_agregar_comentario = tk.Button(ventana, text="Agregar Comentario", command=agregar_comentario)
boton_agregar_comentario.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la interfaz
ventana.mainloop()
