<sub>[Leer en español](README.es.md)</sub>

# AI Image Enhancer

A web application created to improve blurred faces with AI. Now with background and scratch repairing.

## Tech Stack

Main Python libraries used in this project:

| Library | Use |
| :--- | :--- |
| **Streamlit** | Web UI framework |
| **OpenCV (cv2)** |  Image processing and manipulation |
| **Pillow (PIL)** | Image format conversion |
| **NumPy** | Numerical computing |

---

### Features:
The app is made in Python with mainly streamlit for UI and 
OpenCV, TensorFlow, and PIL for image processing and deep learning.
It is structured to be simple and modular so you can:

- Load an image
- Apply enhancement filters
- Save the result image

This project uses this pre-trained AI models**:

| Model | Use |
| :--- | :--- |
| **GFPGANv1.4.pth** | Face restoration model |
| **RealESRGAN_x2plus.pth** | Upscaling and background enhancement |


**Main components:**
- app.py: app core, it joins every streamlit modules from ui.py with the models operations
- ui.py: streamlit app visual modules
- utils.py: some utils to image uploading and image format convert
- models.py: ImageEnhancer class core, which includes model loading and operation functions
- config.py: model configurations and streamlit css styling

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/EvolvedAdrian/image-enhancer.git
    ```
2. **Navigate to the directory:**
    ```bash
    cd image-enhancer
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Start the application using:

```bash
streamlit run app.py
```

---
