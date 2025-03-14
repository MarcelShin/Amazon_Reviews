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
from scipy.stats import binom
from scipy.stats import poisson
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

st.write(" \n ")

selected_chart = st.selectbox(
    "Selecione o gráfico que deseja visualizar:",
    options=[
        "Distribuição de Poisson ⭐",
        "Análise de Polaridade",
        "Distribuição Binomial 📊",
        "Análise de Sentimento"
    ]
)

if selected_chart == "Distribuição de Poisson ⭐":
    st.header("Distribuição de Poisson")
    st.write("#### Fórmula da Distribuição de Poisson")
    st.latex(r"P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}")

    def plot_distribution(x, y, title, x_label, y_label):
        fig = px.bar(x=x, y=y,
                title=title,
                labels={x_label: x_label, y_label: y_label},
                text_auto=True, 
                color=x,
                color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns([0.3,0.7])

    # Slider para a taxa média de ocorrência (λ) e o número de eventos desejados
    lambd = col1.number_input("Taxa média de ocorrência (λ):", min_value=0.001, step=0.01, value=2.0)
    x_max = col1.number_input("Número de eventos desejado", min_value=0, step=1, value=20)

    # Cálculo da distribuição de Poisson
    x = np.arange(0, x_max + 1)  # Ajustando x para que inclua o valor máximo
    y = stats.poisson.pmf(x, lambd)

    # Criando a tabela de probabilidades
    df_poisson = pd.DataFrame({
        "X": x,
        "P(X)": y,
        "P(X ≤ k) (Acumulado)": np.cumsum(y),
        "P(X > k) (Acumulado Cauda Direita)": 1 - np.cumsum(y)
    }).set_index("X")

    # Exibindo a tabela de probabilidades
    col2.write("Tabela de probabilidades:")
    col2.write(df_poisson)

    # Gerando o gráfico de Poisson
    plot_distribution(x, y, "Distribuição de Poisson", "Número de eventos", "Probabilidade")

    st.subheader("Interpretação da Tabela:")

    st.write("- Coluna X: Representa o número de eventos observados.")
    st.write("- Coluna P(X): Probabilidade exata de que ocorra exatamente *X* eventos.")
    st.write("- Coluna P(X≤k acumulado): Probabilidade acumulada de que ocorra até *k* eventos.")
    st.write("- Coluna P(X>k acumulado Cauda Direita): Probabilidade de ocorrer mais que *k* eventos.")

    st.subheader("Exemplo de Interpretação")

    st.write(r"- A probabilidade de que exatamente 2 eventos ocorram é 0.2707 (ou seja, cerca de 27% das vezes teremos 2 eventos).")
    st.write(r"- A probabilidade de que ocorram no máximo 2 eventos *(P(X>2))* é 0.6767, ou seja, há cerca de 67,67% de chance de que o número de eventos seja 0, 1 ou 2.")
    st.write(r"- A probabilidade de que ocorram mais de 2 eventos *(P(X>2))* é 0.3233, ou seja, cerca de 32,33% das vezes o número de eventos será 3 ou mais.")
    
    

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


elif selected_chart == "Distribuição Binomial 📊":
    st.header("Distribuição Binomial")
    st.write("A distribuição binomial modela o número de sucessos em um conjunto fixo de tentativas independentes, onde cada tentativa tem uma probabilidade constante de sucesso. A função de probabilidade da distribuição binomial é:")
    st.subheader("Fórmula da Distribuição Binomial")
    st.latex(r"P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}")

    st.subheader("Onde:")
    st.write("- *X* é o número de sucessos observados.")
    st.write("- *n* é o número total de tentativas.")
    st.write("- *k* é o número de sucessos desejados.")
    st.write("- *p* é a probabilidade de sucesso em cada tentativa.")
    st.write("- (n k) é o coeficiente binomial, que representa o número de maneiras de obter *k* sucessos em *n* tentativas.")

    st.divider()

    def plot_distribution(x, y, title, x_label, y_label):
        fig = px.bar(x=x, y=y,
                 title=title,
                 labels={x_label: x_label, y_label: y_label},
                 text_auto=True,
                 color=x,
                 color_continuous_scale="Blues")
        st.plotly_chart(fig)

    col1, col2 = st.columns([0.5, 0.5])

    # Definindo o slider para o número máximo de tentativas (n_max)
    n_max = col1.number_input("Número máximo de tentativas", value=50)
    
    # Slider para o número de tentativas (n) e número de sucessos (k)
    n = col1.slider("Número de tentativas (n):", min_value=1, max_value=n_max, value=10, step=1)
    k = col2.slider("Número de sucessos (k):", min_value=0, max_value=n, value=5, step=1)
    
    # Slider para a probabilidade de sucesso (p)
    p = col2.slider("Probabilidade de sucesso (p):", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    
    # Gerando a distribuição binomial
    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)
    
    # Criando a tabela de probabilidades
    df_binomial = pd.DataFrame({
        "X": x,
        "P(X)": y,
        "P(X ≤ k) (Acumulado)": np.cumsum(y)
    }).set_index("X")
    
    st.write("Tabela de probabilidades:")
    st.write(df_binomial)

    st.subheader("Exemplo de interpretação:")

    st.write("- A probabilidade de obter exatamente 5 sucessos em 10 tentativas é 0.2461 (24,61%).")
    st.write("- A probabilidade de obter até 5 sucessos (P(X≤5)) é 0.623 (62,3%).")
    st.write("- A probabilidade de obter mais de 5 sucessos (P(X>5))  pode ser calculada como: 1 - 0.623 = 0.377 (37,7%)")
    
    # Plotando a distribuição binomial
    plot_distribution(x, y, "Distribuição Binomial", "Número de sucessos", "Probabilidade")


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