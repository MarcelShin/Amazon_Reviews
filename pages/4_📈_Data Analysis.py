import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import *

st.set_page_config(page_title="Portfólio & Business Analytics", layout="wide")

st.logo("amazon_logo.webp")

st.title("Visualização dos dados")
st.write(" ##### Conjunto de um dataset da Google, utilizado com o intuito de entender melhor sobre a avaliação do uso da Amazon na Google Play.")
st.write(" \n ")

@st.cache_data
def load_data():
    df = pd.read_csv("amazon_reviews.csv")
    return df

df = load_data()

st.write(df.head(5))

st.title("Identificação das variaveis")
df["at"] = pd.to_datetime(df["at"])
tipos_variaveis = df.dtypes
st.table(tipos_variaveis)

st.title("Medidas Centrais & Dispersão")
st.write(df.describe())


selected_chart = st.selectbox(
    "Selecione o gráfico que deseja visualizar:",
    options=[
        "Distribuição das Avaliações ⭐",
        "Análise de Polaridade",
        "Distribuição Probabilística 📊",
        "Análise de Sentimento"
    ]
)

if selected_chart == "Distribuição das Avaliações ⭐":
    st.write("### Distribuição das Avaliações")

    # Criar gráfico de distribuição com Plotly
    fig = px.histogram(df, x="score", nbins=5, marginal="rug", opacity=0.7, 
                       title="Distribuição das Avaliações", 
                       labels={"score": "Avaliação"})

    # Exibir no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    

elif selected_chart == "Análise de Polaridade":
    st.write("### Análise de Polaridade")

    # Contar quantas vezes cada score aparece
    df_polaridade = df["score"].value_counts().reset_index()
    df_polaridade.columns = ["score", "quantidade"]

    # Criar gráfico de barras com Plotly
    fig = px.bar(df_polaridade, 
                 x="score", y="quantidade",
                 title="Análise de Polaridade dos Comentários",
                 labels={"score": "Estrela(s)", "quantidade": "Quantidade"},
                 text_auto=True)

    st.plotly_chart(fig, use_container_width=True)


elif selected_chart == "Distribuição Probabilística 📊":
    st.write("### Aplicação de Distribuições Probabilísticas")

    df_prob = df["score"].value_counts(normalize=True).reset_index()
    df_prob.columns = ["score", "probabilidade"]

    fig = px.bar(df_prob, 
                 x="score", y="probabilidade",
                 title="Distribuição Probabilística das Avaliações",
                 labels={"score": "Nota", "thumbsUpCount": "Probabilidade"},
                 text_auto=True,
                 color="score",
                 color_continuous_scale="blues")

    st.plotly_chart(fig, use_container_width=True)


elif selected_chart == "Análise de Sentimento":
    st.write("### Análise de Sentimento dos Comentários")

    df["sentiment"] = df["score"].apply(lambda x: "Comentários Positivos" if x >= 4 else "Comentários Negativos")

    df_sentiment = df["sentiment"].value_counts().reset_index()
    df_sentiment.columns = ["sentimento", "quantidade"]

    fig = px.bar(df_sentiment, 
                 x="sentimento", y="quantidade", 
                 title="Análise de Sentimento dos Comentários",
                 labels={"sentimento": "Sentimento", "quantidade": "Quantidade"},
                 text_auto=True,
                 color="sentimento",
                 color_discrete_map={"Comentários Positivos": "green", "Comentários Negativos": "red"})

    st.plotly_chart(fig, use_container_width=True)