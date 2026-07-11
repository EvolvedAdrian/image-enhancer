# AI Image Enhancer

Una aplicación web creada para mejorar rostros borrosos con IA. Ahora con reparación de fondo y de arañazos.

## Tecnologías

Librerías de Python utilizadas en este proyecto:

| Librería | Uso |
| :--- | :--- |
| **Streamlit** | Framework de interfaz web |
| **OpenCV (cv2)** | Procesamiento y manipulación de imágenes |
| **Pillow (PIL)** | Conversión de formatos de imagen |
| **NumPy** | Computación numérica |

---

### Características:
La aplicación está hecha en Python, principalmente con streamlit para la interfaz de usuario y
OpenCV, TensorFlow y PIL para el procesamiento de imágenes y el aprendizaje profundo.
Está estructurada para ser sencilla y modular, de forma que puedas:

- Cargar una imagen
- Aplicar filtros de mejora
- Guardar la imagen resultante

Este proyecto utiliza estos modelos de IA preentrenados:

| Modelo | Uso |
| :--- | :--- |
| **GFPGANv1.4.pth** | Modelo de restauración facial |
| **RealESRGAN_x2plus.pth** | Escalado y mejora de fondo |


**Componentes principales:**
- app.py: núcleo de la aplicación, une todos los módulos de streamlit de ui.py con las operaciones de los modelos
- ui.py: módulos visuales de la aplicación streamlit
- utils.py: algunas utilidades para la carga de imágenes y la conversión de formatos de imagen
- models.py: núcleo de la clase ImageEnhancer, que incluye la carga de modelos y las funciones de operación
- config.py: configuraciones de modelos y estilos CSS de streamlit

---

## Primeros Pasos

### Requisitos previos

- Python 3.8 o superior
- Gestor de paquetes pip

### Instalación

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/EvolvedAdrian/image-enhancer.git
    ```
2. **Navega al directorio:**
    ```bash
    cd image-enhancer
    ```
3. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Uso

Inicia la aplicación con:

```bash
streamlit run app.py
```

---
