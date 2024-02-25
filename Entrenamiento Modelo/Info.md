    Preprocesamiento de Imágenes: 
Se utiliza ImageDataGenerator de TensorFlow para preprocesar las imágenes antes de alimentarlas al modelo. 
Esto incluye la normalización y el aumento de datos, lo que ayuda a mejorar la generalización del modelo.

    Transfer Learning: 
Se utiliza VGG16 como base convolucional pre-entrenada. 
Esta técnica, conocida como transfer learning, aprovecha el conocimiento aprendido por un 
modelo en un conjunto de datos grande y general para resolver un problema diferente pero relacionado.

    Callbacks: 
Se utilizan callbacks como ModelCheckpoint y EarlyStopping para monitorear el progreso del modelo durante 
el entrenamiento. ModelCheckpoint guarda el mejor modelo según una métrica específica, mientras que EarlyStopping
detiene el entrenamiento si no hay mejoras en una métrica de validación durante un número específico de épocas.

    Visualización de Métricas: 
Las métricas de entrenamiento y validación (precisión y pérdida) se visualizan utilizando matplotlib.pyplot. 
Esto proporciona una comprensión visual del rendimiento del modelo a lo largo del tiempo y ayuda a identificar 
problemas como sobreajuste o subajuste.

    Evaluación del Modelo: 
Una vez que el modelo se ha entrenado, se evalúa su rendimiento utilizando los datos de prueba. 
Esto proporciona una estimación objetiva de cómo se desempeñará el modelo en datos no vistos en la práctica.

    Guardar el Mejor Modelo: 
El modelo con el mejor desempeño en datos de validación se guarda en un archivo llamado "best_model.h5" 
utilizando ModelCheckpoint. Este modelo puede ser utilizado más tarde para hacer predicciones en nuevos datos 
sin necesidad de volver a entrenar.
