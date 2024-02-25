
import os
import csv

def crear_csv_con_imagenes(directorio_imagenes, nombre_archivo_csv):
    # Lista para almacenar los datos de las imágenes
    datos_imagenes = []

    # Recorre el directorio de imágenes
    for root, _, archivos in os.walk(directorio_imagenes):
        for archivo in archivos:
            # Verifica si el archivo es una imagen
            if archivo.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Obtiene la ruta completa del archivo
                ruta_completa = os.path.join(root, archivo)
                # Obtiene el nombre de la imagen
                nombre_imagen = archivo
                # Agrega el nombre de la imagen y su ruta a la lista de datos
                datos_imagenes.append([nombre_imagen, ruta_completa])

    # Escribe los datos en un archivo CSV
    with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribe los encabezados
        escritor_csv.writerow(['Nombre', 'Ruta'])
        # Escribe los datos de las imágenes
        escritor_csv.writerows(datos_imagenes)

# Directorio donde se encuentran las imágenes
directorio_imagenes = '/Users/juanmi-macbook/Desktop/Programa - Sitemas Inteligentes/Diseño/Prototipo/Dataset/TB_Chest_Radiography_Database/Tuberculosis'

# Nombre del archivo CSV que se va a crear
nombre_archivo_csv = '/Users/juanmi-macbook/Desktop/Programa - Sitemas Inteligentes/imagenes.csv'

# Llama a la función para crear el archivo CSV
crear_csv_con_imagenes(directorio_imagenes, nombre_archivo_csv)
