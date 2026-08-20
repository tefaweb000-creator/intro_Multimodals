import streamlit as st
from PIL import Image 

st.title("Tengo más trabajos que vida")
st.header ("ya no aguanto más")
st.write("y tengo hambre")
image= Image.open("perrolllora.png")
st.image(image,caption= "interfaces multimodales")

texto= st.text_input ("¿qué puedo tragar?")
st.write("el texto escrito es", texto)
st.subheader ("ahora usamos dos columnas")
col1,col2 = st.columns(2)

with col1;
    st.subheader ("primera")
    st.write("el texto escrito es", texto)
    resp = st.checkbox ("estoy de acuerdo")
    if resp; st.write ("correcto")

with col2:
  st.subheader ("y la otra")
modo= st.radio ("qué modalidad es esto", ("visual", "auditiva", "táctil"))

                      
      
