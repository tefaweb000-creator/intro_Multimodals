limport streamlit as st
from PIL import image 

st.title("Tengo más trabajos que vida")
st.header ("ya no aguanto más")
st.write("y tengo hambre")
image= Image.open("perrollora.png")
st.Image(image,caption= "interfaces multimodales")
