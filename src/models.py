from gfpgan import GFPGANer
from config import CONFIG
from zeroscratches import EraseScratches
from src.utils import bgr_to_pil, pil_to_bgr
import streamlit as st

class ImageEnhancer:
    """Class to manage GFPGAN model and image processing"""
    def __init__(self):
        self.model = None
        self._scratch_eraser = None

    @property
    def scratch_eraser(self):
        if self._scratch_eraser is None:
            self._scratch_eraser = EraseScratches()
        return self._scratch_eraser
    
    def _remove_scratches(self, img_bgr):
        """Remove stripes and scratches from image before passing into GFPGAN"""
        pil_img = bgr_to_pil(img_bgr)
        restored_rgb = self.scratch_eraser.erase(pil_img)
        restored_bgr = pil_to_bgr(restored_rgb)
        return restored_bgr

    @st.cache_resource
    def load_model_simple(_self):
        """Loads GFPGAN model for face enhancement"""
        model = GFPGANer(
            model_path=CONFIG["model_url"],
            upscale=CONFIG["upscale"],
            arch=CONFIG["arch"],
            channel_multiplier=CONFIG["channel_multiplier"],
            bg_upsampler=None
        )
        return model
    
    def enhance(self, image_bgr, repair_scratches=False):
        """Enhances an image with customizable options

        Args:
            image_bgr: Image in BGR format
        """
        if repair_scratches:
            st.info("Reparando grietas y arañazos...")
            image_bgr = self._remove_scratches(image_bgr)
        
        if not self.model:
            self.model = self.load_model_simple()
        
        _, _, restored_img = self.model.enhance(
            image_bgr,
            has_aligned=False,
            only_center_face=False,
            paste_back=True,
            weight=CONFIG["enhancement_weight"]
        )
        return restored_img