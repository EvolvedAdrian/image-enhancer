PAGE_CONFIG = {
    "page_title": "AI Photo Enhancer",
    "page_icon": "💫",
    "layout": "centered"
}

STYLE_CONFIG = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap');

* {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.stApp {
    background: linear-gradient(120deg, #3D3155, #53568F);
}

header { visibility: hidden; }

a[href^="#"] { display: none; }

#photo-face-enhancer {
    background: linear-gradient(120deg, #817ec2, #e8d1d6);
    background-clip: text;
    color: transparent;
}

.stButton > button {
    border: 1px solid #eee3;
    background: linear-gradient(10deg, #3D3155, #53568F, #3D3155);
    background-size: auto 400%;
    background-position: top;
    transition: all 0.2s;

    &:hover{
        border: 1px solid #eee3;
        background-position: bottom;
    }
}

.stDownloadButton > button {
    border: 1px solid #eee3;
    background-color: #1a1533;
    transition: all 0.2s;

    &:hover{
        border: 1px solid #eee3;
        background-color: #3D3155;
    }
}

div.stFileUploader > section {
    box-shadow: 3px 3px 10px 3px #15153d;
    background: linear-gradient(120deg, #3D3155, #1a1533);
}

.stSlider > div > div > div {
    & > div {
        background-image: linear-gradient(90deg, #817ec2, #e8d1d6);
        & > div {
            background-color: #1a1533;
            box-shadow: none;
            & > div {
                color: #e8d1d6;
            }
        }
    }
}



</style>
"""

CONFIG = {
    # GFPGAN Model
    "model_url": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth",
    "upscale": 1,
    "arch": "clean",
    "channel_multiplier": 2,
    "enhancement_weight": 0.5,

    # Allowed formats
    "allowed_formats": ['jpg', 'jpeg', 'png']
}