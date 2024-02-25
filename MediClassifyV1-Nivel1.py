"""
Descripción General:

Este script de Python implementa una interfaz gráfica de usuario (GUI) utilizando la biblioteca Tkinter para cargar un archivo CSV que contiene rutas de imágenes. Las primeras cinco imágenes del archivo CSV se muestran en un lienzo de Tkinter. El usuario puede navegar entre las imágenes y realizar un pre diagnóstico sobre la imagen actual.
Módulos Importados:

    tkinter: Biblioteca estándar de Python para crear interfaces gráficas de usuario.
    PIL: Python Imaging Library, utilizada para manejar imágenes.
    cv2: OpenCV, una biblioteca de visión por computadora y procesamiento de imágenes.
    pandas: Biblioteca para el análisis de datos en Python.
    os: Módulo para la interacción con el sistema operativo.

Clase GUI:

    Método __init__:
        Configura la ventana principal de la interfaz gráfica con diferentes widgets como botones, etiquetas y un lienzo.
    Método load_csv:
        Abre un cuadro de diálogo para seleccionar un archivo CSV y carga las rutas de las imágenes del archivo CSV en una lista.
    Método show_image:
        Muestra la imagen en el lienzo utilizando la ruta de la imagen proporcionada.
    Métodos show_next_image y show_previous_image:
        Permiten navegar entre las imágenes cargadas hacia adelante y hacia atrás.
    Método process_images:
        Realiza un pre diagnóstico de la imagen actualmente mostrada.
    Método pre_diagnostico_imagen:
        Realiza el pre diagnóstico de la imagen utilizando su nombre.
    Método quit_program:
        Cierra la aplicación.

Ejecución Principal:

    Se instancia un objeto de la clase GUI y se inicia el bucle principal del programa con mainloop().

Notas Adicionales:

    Se limita a mostrar solo las primeras cinco imágenes del archivo CSV cargado.
    El pre diagnóstico actual simplemente devuelve un mensaje de texto con el nombre de la imagen.
"""


import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import pandas as pd
import os


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Prototipo - Nivel 1")
        self.geometry("600x1000")
        self.configure(background="#1e1e1e")

        self.label_path = tk.Label(self, text="Selecciona un archivo CSV:", font=(
            "Helvetica", 14), bg="#1e1e1e", fg="white")
        self.label_path.pack(pady=10)

        self.btn_browse = tk.Button(self, text="Seleccionar archivo CSV", command=self.load_csv, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_browse.pack(pady=5)

        self.canvas_frame = tk.Frame(self, bg="#1e1e1e")
        self.canvas_frame.pack(padx=50, pady=10, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(
            self.canvas_frame, width=500, height=300, bg="#1e1e1e", bd=2, relief=tk.SOLID)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.btn_prev_image = tk.Button(self, text="Anterior Imagen", command=self.show_previous_image, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_prev_image.pack(pady=5)

        self.btn_next_image = tk.Button(self, text="Siguiente Imagen", command=self.show_next_image, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_next_image.pack(pady=5)

        self.label_instructions = tk.Label(self, text="Las primeras 5 imágenes del archivo CSV se mostrarán aquí.", font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.label_instructions.pack(pady=10)

        self.label_image_name = tk.Label(self, text="", font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.label_image_name.pack(pady=5)

        self.image_counter = tk.StringVar()
        self.label_image_counter = tk.Label(self, textvariable=self.image_counter, font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.label_image_counter.pack(pady=5)

        self.btn_process = tk.Button(self, text="Analizar Imágenes", command=self.process_images, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_process.pack(pady=5)

        self.diagnostico_label = tk.Label(self, text="", font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.diagnostico_label.pack(pady=5)

        self.btn_exit = tk.Button(self, text="Salir", command=self.quit_program, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_exit.pack(pady=5)

        self.current_image_idx = 0
        self.image_paths = []

    def load_csv(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.image_paths = pd.read_csv(file_path)['Ruta'].values[:5]
            self.show_image(self.current_image_idx)

    def show_image(self, idx):
        if 0 <= idx < len(self.image_paths):
            path = self.image_paths[idx]
            image = cv2.imread(path)
            # Convert from BGR to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            self.image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
            # Obtener el nombre del archivo de la ruta
            image_name = os.path.basename(path)
            # Actualiza el nombre de la imagen actual
            self.label_image_name.config(
                text="Nombre de la imagen: " + image_name)
            self.image_counter.set(
                f"Imagen {idx + 1} de {len(self.image_paths)}")
            self.current_image_idx = idx

    def show_next_image(self):
        self.current_image_idx = (
            self.current_image_idx + 1) % len(self.image_paths)
        self.show_image(self.current_image_idx)

    def show_previous_image(self):
        self.current_image_idx = (
            self.current_image_idx - 1) % len(self.image_paths)
        self.show_image(self.current_image_idx)

    def process_images(self):
        if not self.image_paths.any():
            messagebox.showerror("Error", "No se han cargado imágenes.")
            return

        # Obtener la ruta de la imagen actual
        current_image_path = self.image_paths[self.current_image_idx]
        # Obtener el nombre de la imagen actual
        image_name = os.path.basename(current_image_path)
        # Realizar el pre diagnóstico de la imagen actual
        pre_diagnostico = self.pre_diagnostico_imagen(image_name)
        # Mostrar el pre diagnóstico en la etiqueta
        self.diagnostico_label.config(text=pre_diagnostico)

    def pre_diagnostico_imagen(self, image_name):
        # Aquí iría el código para el pre diagnóstico de la imagen
        # Por ejemplo, podrías usar técnicas de procesamiento de imágenes
        # para extraer características relevantes y hacer una evaluación preliminar.
        pre_diagnostico = "Pre diagnóstico realizado para la imagen: " + image_name
        return pre_diagnostico

    def quit_program(self):
        self.quit()


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
