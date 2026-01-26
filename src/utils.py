import cv2
import numpy as np
from PIL import Image

def pil_to_bgr(image):
    """Converts PIL image to BGR format (OpenCV)

    Args:
        image: PIL image
    
    Returns:
        numpy array in BGR format
    """
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    return img_bgr

def bgr_to_pil(image_bgr):
    """Converts BGR image (OpenCV) to PIL format

    Args:
        image_bgr: numpy array in BGR format
    
    Returns:
        PIL image
    """
    img_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(img_rgb)
    return pil_image

def load_image(uploaded_file):
    """Loads an image from an uploaded file

    Args:
        uploaded_file: Streamlit uploaded file
    
    Returns:
        PIL image in RGB format
    """
    image = Image.open(uploaded_file).convert('RGB')
    return image