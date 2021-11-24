import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np


@st.cache
def load_model(lang):
    return ocr.Reader([lang], model_storage_directory='.')


def get_key(val, lang):
    for key, value in lang.items():
        if val == value:
            return key


def main():
    st.subheader("Easy OCR - Extract Text from Images")
    st.write("Optical Character Recognition using easyocr and streamlit")
    image = st.file_uploader(label="Upload your image here",
                             type=['png', 'jpg', 'jpeg'])

    lang = {
        "en": "English",
        "hi": "Hindi",
        "kn": "Kannada",
        "ta": "Tamil",
        "te": "Telugu"
    }

    task = list(lang.values())
    feature_choice = st.sidebar.selectbox("Language To Detect: ", task)
    if image is not None:
        input_image = Image.open(image)
        st.image(input_image)
        reader = load_model(lang=get_key(feature_choice, lang=lang))
        with st.spinner("🤖 Extracting... "):
            result = reader.readtext(np.array(input_image))
            result_text = [text[1] for text in result]
            st.write(result_text)
        st.balloons()
    else:
        st.info("Please, Upload an Image to process...")
    st.caption("Made with ❤️ by @Siva Prakash")


if __name__ == "__main__":
    main()
