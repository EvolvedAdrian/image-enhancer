import streamlit as st
from config import CONFIG
from PIL import Image
import numpy as np
import cv2
import io

def render_header():
    """Renders the app header"""
    st.title("Photo Face Enhancer", text_alignment="center")
    st.markdown("Upload and improve your photos with AI", text_alignment="center")

def render_file_uploader():
    """Renders the file uploader component
    
    Returns:
        UploadedFile or None
    """
    uploaded_file = st.file_uploader(
        "Select a photo",
        type=CONFIG["allowed_formats"],
        help="Upload a photo to improve its quality"
    )
    return uploaded_file

def render_interactive_slider(original_img, restored_img):
    """Renders the slider interactive comparator

    Args:
        original_img: Original PIL image
        restored_img: Restored PIL image
    """
    st.markdown("---")
    st.subheader("Interactive comparator", text_alignment="center")

    slider_value = st.slider(
        "Slide to compare",
        min_value = 0,
        max_value=100,
        value=50,
        label_visibility="collapsed"
    )

    # Ensure same size
    if original_img.size != restored_img.size:
        restored_img = restored_img.resize(original_img.size, Image.LANCZOS)
    
    # Create splitted image
    width = original_img.width
    split_pos = int(width * slider_value / 100)

    combined = Image.new('RGB', original_img.size)
    combined.paste(original_img.crop((0, 0, split_pos, original_img.height)))
    combined.paste(restored_img.crop((split_pos, 0, width, original_img.height)), (split_pos, 0))

    # Add dividing line
    combined_array = np.array(combined)
    cv2.line(
        combined_array,                 # Image
        (split_pos, 0),                 # Initial point (xInitial, yInitial)
        (split_pos, combined.height),   # Final point (xFinal, yFinal)
        (255, 255, 255),                # Color
        3                               # Thickness
    )
    st.image(combined_array, width='stretch')

def render_download_button(restored_img):
    """Renders the download button
        
    Args:
        restored_img: Restored PIL image
    """
    buf = io.BytesIO()
    restored_img.save(buf, format='PNG')
    st.download_button(
        label="Download enhanced",
        data=buf.getvalue(),
        file_name="image_enhanced.png",
        mime="image/png",
        width="stretch"
    )