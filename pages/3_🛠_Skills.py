import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Portfólio & Skills", layout="wide")

st.logo("skills-icon.jpg")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("📌 Coluna 1")
    st.write("Conteúdo da primeira coluna.")

with col2:
    st.header("📌 Coluna 2")
    st.write("Conteúdo da segunda coluna.")

with col3:
    st.header("📌 Coluna 2")
    st.write("Conteúdo da segunda coluna.")

st.subheader("🔹 Subtópico 2")
st.write("Descrição ou explicação do subtópico 2.")