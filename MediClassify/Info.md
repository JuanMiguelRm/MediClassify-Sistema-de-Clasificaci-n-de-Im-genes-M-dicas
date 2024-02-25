                                Info Niveles
                                
    
    Nivel 1. 
Prototipo con una interfaz gráfica funcional, que permite ver la implementación de los casos de
uso a nivel de interacción con el usuario. El prototipo recoge los datos, permite visualizarlos,
pero no realiza un procesamiento avanzado. En la documentación del proyecto si se muestra la arquitectura 
del sistemas, los módulos pendientes requeridos, la herramientas, técnias y tecnología a utilizar 
como trabajo futuro.

    Nivel 2. 
Prototipo con una interfaz gráfica funcional, que permite ver la implementación de los casos de uso a nivel 
de interacción con el usuario. El prototipo recoge los datos, permite visualizarlos, y realiza un procesamiento
previo o mostrando resultados parciales o preliminares. En la documentación del proyecto si se muestra 
la arquitectura del sistemas, los módulos pendientes requeridos, la herramientas, técnicas y tecnología 
a utilizar como trabajo futuro.

    
                                  Info General:

Interfaz Gráfica (GUI): 
La clase GUI define la interfaz de usuario utilizando la biblioteca Tkinter de Python. Tkinter es una biblioteca estándar que proporciona widgets y herramientas para crear interfaces gráficas de usuario en aplicaciones de escritorio.

Canvas: 
El lienzo (canvas) se utiliza para mostrar las imágenes. Se crea dentro de un marco (canvas_frame) para permitir su expansión y relleno según el tamaño de la ventana.

Botones y Etiquetas: 
Se utilizan botones y etiquetas para interactuar con el usuario y mostrar información relevante, como la selección de modelos, instrucciones, nombre de la imagen actual y diagnósticos.

Procesamiento de Imágenes: 
El método process_images utiliza un modelo pre-entrenado para realizar la clasificación de las imágenes cargadas en la interfaz. Muestra el diagnóstico resultante en la etiqueta diagnostico_label.
