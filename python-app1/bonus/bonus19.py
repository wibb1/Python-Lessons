import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    photo = st.camera_input("Camera")

if photo:
    img = Image.open(photo)

    grey_image = img.convert('L')
    st.image(grey_image)

uploaded = st.file_uploader("Upload Image")