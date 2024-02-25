# Importar las bibliotecas necesarias
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import pandas as pd
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Definir la clase GUI


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Clasificación de Imágenes de Rayos X de Tórax")
        self.geometry("600x1000")
        self.configure(background="#1e1e1e")

        # Etiqueta para mostrar el camino del modelo
        self.label_model_path = tk.Label(self, text="Selecciona el modelo pre-entrenado:", font=(
            "Helvetica", 14), bg="#1e1e1e", fg="white")
        self.label_model_path.pack(pady=10)

        # Botón para seleccionar el modelo pre-entrenado
        self.btn_browse_model = tk.Button(self, text="Seleccionar modelo", command=self.load_model, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_browse_model.pack(pady=5)

        # Etiqueta para mostrar el camino del archivo CSV
        self.label_path = tk.Label(self, text="Selecciona un archivo CSV:", font=(
            "Helvetica", 14), bg="#1e1e1e", fg="white")
        self.label_path.pack(pady=10)

        # Botón para seleccionar el archivo CSV
        self.btn_browse = tk.Button(self, text="Seleccionar archivo CSV", command=self.load_csv, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_browse.pack(pady=5)

        # Marco para el lienzo de las imágenes
        self.canvas_frame = tk.Frame(self, bg="#1e1e1e")
        self.canvas_frame.pack(padx=50, pady=10, fill=tk.BOTH, expand=True)

        # Lienzo para mostrar las imágenes
        self.canvas = tk.Canvas(
            self.canvas_frame, width=500, height=300, bg="#1e1e1e", bd=2, relief=tk.SOLID)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Botones para navegar entre las imágenes
        self.btn_prev_image = tk.Button(self, text="Anterior Imagen", command=self.show_previous_image, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_prev_image.pack(pady=5)

        self.btn_next_image = tk.Button(self, text="Siguiente Imagen", command=self.show_next_image, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_next_image.pack(pady=5)

        # Etiqueta para mostrar las instrucciones
        self.label_instructions = tk.Label(self, text="Las primeras 5 imágenes del archivo CSV se mostrarán aquí.", font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.label_instructions.pack(pady=10)

        # Etiqueta para mostrar el nombre de la imagen actual
        self.label_image_name = tk.Label(self, text="", font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.label_image_name.pack(pady=5)

        # Etiqueta para mostrar el número de imagen actual
        self.image_counter = tk.StringVar()
        self.label_image_counter = tk.Label(self, textvariable=self.image_counter, font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.label_image_counter.pack(pady=5)

        # Botón para procesar las imágenes
        self.btn_process = tk.Button(self, text="Analizar Imágenes", command=self.process_images, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_process.pack(pady=5)

        # Etiqueta para mostrar el pre diagnóstico
        self.diagnostico_label = tk.Label(self, text="", font=(
            "Helvetica", 12), bg="#1e1e1e", fg="white")
        self.diagnostico_label.pack(pady=5)

        # Botón para salir del programa
        self.btn_exit = tk.Button(self, text="Salir", command=self.quit_program, font=(
            "Helvetica", 12), bg="#ffc107", fg="black", activebackground="#ffc107", activeforeground="black")
        self.btn_exit.pack(pady=5)

        # Variables de clase
        self.current_image_idx = 0
        self.image_paths = []
        self.model = None

    # Método para cargar el modelo pre-entrenado
    def load_model(self):
        model_path = filedialog.askopenfilename(
            filetypes=[("H5 files", "*.h5")])
        if model_path:
            self.model = load_model(model_path)

    # Método para cargar el archivo CSV
    def load_csv(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.image_paths = pd.read_csv(file_path)['Ruta'].values[:5]
            self.show_image(self.current_image_idx)

    # Método para mostrar la imagen actual
    def show_image(self, idx):
        if 0 <= idx < len(self.image_paths):
            path = self.image_paths[idx]
            image = cv2.imread(path)
            # Convertir de BGR a RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            self.image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
            # Obtener el nombre del archivo de la ruta
            image_name = os.path.basename(path)
            # Actualizar el nombre de la imagen actual
            self.label_image_name.config(
                text="Nombre de la imagen: " + image_name)
            self.image_counter.set(
                f"Imagen {idx + 1} de {len(self.image_paths)}")
            self.current_image_idx = idx

    # Método para mostrar la siguiente imagen
    def show_next_image(self):
        self.current_image_idx = (
            self.current_image_idx + 1) % len(self.image_paths)
        self.show_image(self.current_image_idx)

    # Método para mostrar la imagen anterior
    def show_previous_image(self):
        self.current_image_idx = (
            self.current_image_idx - 1) % len(self.image_paths)
        self.show_image(self.current_image_idx)

    # Método para procesar las imágenes
    def process_images(self):
        if not self.model:
            messagebox.showerror("Error", "Por favor selecciona un modelo.")
            return
        if not self.image_paths.any():
            messagebox.showerror("Error", "No se han cargado imágenes.")
            return

        # Realizar la clasificación de las imágenes
        diagnoses = []
        for path in self.image_paths:
            image = load_img(path, target_size=(224, 224)
                             )  # Redimensionar la imagen
            image = img_to_array(image) / 255.0  # Normalizar la imagen
            # Añadir dimensión del lote
            image = image.reshape(
                (1, image.shape[0], image.shape[1], image.shape[2]))
            prediction = self.model.predict(image)
            # Convertir las probabilidades en diagnósticos según tu lógica de clasificación
            diagnosis = "Neumonía" if prediction[0][0] > 0.5 else "Normal"
            diagnoses.append(diagnosis)

        # Mostrar los diagnósticos
        self.diagnostico_label.config(
            text="Diagnósticos: " + ", ".join(diagnoses))

    # Método para salir del programa
    def quit_program(self):
        self.destroy()


# Instanciar y ejecutar la aplicación
app = GUI()
app.mainloop()
