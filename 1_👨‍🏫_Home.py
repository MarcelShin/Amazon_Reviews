import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

# Configuração da página
st.set_page_config(page_title="Portfólio & Business Analytics", layout="wide")

# Adicionando o logo no body - "Sobre mim"

col1, col2 = st.columns(2)

with col1:
    st.image("profile_foto_marcelo.jfif", width=350)

with col2:
    st.title("Bem-vindo ao meu Portfólio!")
    st.write("Olá, me chamo Marcelo! Atualmente, atuo na área de Governança de Tecnologia, e utilizo de muitos dados para minhas rotinas de análise.")
    st.write("Sou apaixonado por tecnologia e sempre em busca de novos desafios, gosto de explorar soluções inovadoras e aprender algo novo a cada dia. Tenho um perfil curioso, analítico e focado em encontrar as melhores estratégias para resolver problemas. Acredito que a inovação e a constante evolução são essenciais para crescer profissionalmente!")




st.subheader("🎯 Objetivo")
st.write("Meu objetivo é me desenvolver, enquanto aplico meus conhecimentos no ambiente corporativo e aprimoro minhas skills!")