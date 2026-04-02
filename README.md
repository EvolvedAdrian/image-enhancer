# AI Image Enhancer
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

> A web application to improve blurred faces with AI. Now with background and scratch repairing. It is structured to be simple and modular so you can:
- Load an image
- Apply enhancement filters
- Save the result image

### Project operation:
The app is made in Python with mainly streamlit for UI and 
OpenCV, TensorFlow, and PIL for image processing and deep learning

This project uses this pre-trained AI models**:

| Model | Purpose | Framework |
| :--- | :--- | :--- |
| **GFPGANv1.4.pth** | Face restoration model |
| **RealESRGAN_x2plus.pth** | Upscaling and background enhancement |


**Main components:**
- app.py: app core, it joins every streamlit modules from ui.py with the models operations
- ui.py: streamlit app visual modules
- utils.py: some utils to image uploading and image format convert
- models.py: ImageEnhancer class core, which includes model loading and operation functions
- config.py: model configurations and streamlit css styling

---

## 📦 Dependencies

Main Python libraries used in this project:

| Library | Use |
| :--- | :--- |
| **Streamlit** | Web UI framework |
| **OpenCV (cv2)** |  Image processing and manipulation |
| **Pillow (PIL)** | Image format conversion |
| **NumPy** | Numerical computing |

---

## 🚀 Getting Started

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

---

## 💻 Usage

Start the application using:

```bash
npm run start
```

---

## Author

👤 **Adrián**

* Github: [@EvolvedAdrian](https://github.com/EvolvedAdrian)

