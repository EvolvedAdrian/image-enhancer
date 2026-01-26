from src.models import ImageEnhancer
from src.utils import pil_to_bgr, bgr_to_pil, load_image

def main():
    # Load image as PIL using helper function
    with open("./image.jpg", "rb") as f:
        image_pil = load_image(f)

    # Convert from PIL to BGR
    image_bgr = pil_to_bgr(image_pil)

    # Create enhancer object and restore image
    enhancer = ImageEnhancer()
    restored_bgr = enhancer.enhance(image_bgr)

    # Convertir de BGR a PIL
    restored_pil = bgr_to_pil(restored_bgr)

    # Save image to disk
    restored_pil.save("./image_restored.jpg")

if __name__ == "__main__":
    main()