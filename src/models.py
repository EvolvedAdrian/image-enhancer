from gfpgan import GFPGANer
from config import CONFIG_GFPGAN, CONFIG_RRDBNET, CONFIG_UPSAMPLER
from zeroscratches import EraseScratches
from src.utils import bgr_to_pil, pil_to_bgr
import streamlit as st
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

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
    def load_model_simple(_self, _bg_upsampler=None):
        """Loads GFPGAN model for face enhancement"""
        model = GFPGANer(
            model_path=CONFIG_GFPGAN["model_url"],
            upscale=CONFIG_GFPGAN["upscale"],
            arch=CONFIG_GFPGAN["arch"],
            channel_multiplier=CONFIG_GFPGAN["channel_multiplier"],
            bg_upsampler=_bg_upsampler
        )
        return model
    
    def load_model_with_background(self):
        """Loads GFPGAN with RealESRGAN (face enhancer + background)"""
        model_bg = RRDBNet(**CONFIG_RRDBNET)

        bg_upsampler = RealESRGANer(
            **CONFIG_UPSAMPLER,
            model = model_bg
        )
        
        return self.load_model_simple(bg_upsampler)
    
    def enhance(self, image_bgr, repair_scratches=False, enhance_background=False):
        """Enhances an image with customizable options
        
        Args:
            image_bgr: Image in BGR format
        """
        if repair_scratches:
            st.info("Repairing stripes and scratches...")
            image_bgr = self._remove_scratches(image_bgr)
        
        if not self.model:
            if enhance_background:
                st.info("Enhancing faces and background...")
                self.model = self.load_model_with_background()
            else:
                st.info("Enhancing faces...")
                self.model = self.load_model_simple()
        
        _, _, restored_img = self.model.enhance(
            image_bgr,
            has_aligned=False,
            only_center_face=False,
            paste_back=True,
            weight=CONFIG_GFPGAN["enhancement_weight"]
        )
        return restored_img