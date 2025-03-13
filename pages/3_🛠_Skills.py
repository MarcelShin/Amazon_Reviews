import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Portfólio & Skills", layout="wide")

st.logo("skills-icon.jpg")

st.header("🔹 Competências técnicas (Hard Skills)")
st.subheader("👨‍🔬 Ciência de Dados & IA")
st.write("- Machine Learning: TensorFlow, PyTorch, Scikit-Learn.")
st.write("- Análise de Dados: Pandas, Matplotlib, Power BI.")
st.write("- Processamento de Linguagem Natural (NLP): LangChain, OpenAI API.")

st.subheader("👨‍💻 Banco de Dados & Big Data")
st.write("- SQL (MySQL).")
st.write("- NoSQL (MongoDB).")
st.write("- Processamento de Dados: Apache Spark.")
