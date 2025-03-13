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
st.write(" ##### Conjunto de um dataset da Google Play, utilizado com o intuito de entender melhor sobre a avaliação da Amazon na Google Play.")
st.write(" \n ")

@st.cache_data
def load_data():
    df = pd.read_csv("amazon_reviews.csv")
    return df

df = load_data()

st.write(df.head(5))

st.title("Identificação das variaveis")
st.write(" 1. reviewId - Qualitativa | Utilizada para ordenar os IDs.")
st.write(" 2. userName - Quantitativa | Não depende de ordem, servindo apenas para identificação dos Users.")
st.write(" 3. content - Quantitativa | Não possui ordem, considernado que é apenas o comentário, e não possui critério para ordenar.")
st.write(" 4. score - Qualitativa | Deve ser ordenada para identificarmos as maiores estrelas, seguindo até as menores estrelas das avaliações.")
st.write(" 5. thumbsUpCount - Qualitativa | Ordenar para ver as avaliações com maiores curtidas.")
st.write(" 6. reviewCreatedVersion - Qualitativa | Utilizando a ordem das versões da review, para avaliações de versões mais recentes.")
st.write(" 7. at - Qualitativa | Ordenada, para identificar as avaliações mais recentes.")
st.write(" 8. appVersion - Qualitativa | Utilizando a ordem das versões do app, para avaliações de versões mais recentes.")

st.title("Medidas Centrais & Dispersão")
st.write(df.describe())
st.markdown(" - Temos um total de 71.172 avaliações, e no todo, a média de estrelas por avaliação é de 2.5")
st.markdown(" - O desvio padrão da média é de 1.7 estrelas")
st.markdown(" - O primeiro quartil (25%), possui as piores avaliações (1), em contra partida, quando observamos o último quartil, identificamos que lá estão as melhores avaliações do app.")
st.markdown(" - De todos os quartis, apenas o último quartil possui 'curtidas' nas avaliações, as demais, estão sem curtidas.")


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
                 color_continuous_scale="reds")

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