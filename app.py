from src.models import ImageEnhancer
from src.utils import (
    pil_to_bgr, 
    bgr_to_pil, 
    load_image
)
from src.ui import (
    render_header,
    render_file_uploader,
    render_interactive_slider,
    render_download_button
)
import streamlit as st
from config import PAGE_CONFIG, STYLE_CONFIG

st.set_page_config(**PAGE_CONFIG)
st.markdown(STYLE_CONFIG, unsafe_allow_html=True)

def main():
    """Main app function"""

    render_header()

    # Initialize model
    enhancer = ImageEnhancer()

    # Upload file
    uploaded_file = render_file_uploader()

    if uploaded_file is not None:
        # Load image
        original_image = load_image(uploaded_file)
        img_bgr = pil_to_bgr(original_image)


        # Processing options
        st.markdown("---")
        st.subheader("Enhancer options")

        col_opt1, col_opt2 = st.columns(2)

        with col_opt1:
            repair_scratches = st.checkbox(
                "Repair scratches",
                value=False,
                help="Remove stripes and scratches from image"
            )
        
        with col_opt2:
            enhance_background = st.checkbox(
                "Enhance background quality",
                value=False,
                help="Use RealESRGAN to enhance background"
            )

        st.markdown("---")

        # Processing button
        if st.button("Improve quality 💫", type="primary", width="stretch"):
            with st.spinner("Processing with AI...⌛"):
                # Improve photo with selected options
                restored_bgr = enhancer.enhance(
                    img_bgr,
                    repair_scratches,
                    enhance_background
                )
                restored_img = bgr_to_pil(restored_bgr)

                # Save image in session state
                st.session_state['restored_img'] = restored_img
                st.session_state['original_img'] = original_image

                st.success("🟢 Success! Photo improved")
                st.rerun()
        
        # Display original image
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original", text_alignment="center")
            st.image(original_image, width="stretch")

        # Show result if exists
        if "restored_img" in st.session_state:
            # Download button
            render_download_button(st.session_state['restored_img'])

            with col2:
                st.subheader("AI Enhanced", text_alignment="center")
                st.image(st.session_state['restored_img'], width='stretch')
            
            # Interactive comparator
            render_interactive_slider(
                st.session_state['original_img'],
                st.session_state['restored_img']
            )


if __name__ == "__main__":
    main()