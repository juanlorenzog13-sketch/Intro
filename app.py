import streamlit as st
from PIL import Image
st.title("Mi primera app")
st.header("blehh :PPPPP")
image = Image.open ("blehhh.jpg")
st.image(image, caption="blehhh")
texto=st.text_input("Ingresa texto","texto inicial")
