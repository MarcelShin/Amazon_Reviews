# Dashboard de Análise de Dados - Google Play Store (Amazon App)

## Sobre o Projeto
Este projeto consiste em um dashboard interativo desenvolvido com Streamlit para visualizar e analisar dados das avaliações do aplicativo da Amazon na Google Play Store. O objetivo é extrair insights sobre as avaliações dos usuários, incluindo distribuições estatísticas, análise de sentimento e polaridade dos comentários.

## Tecnologias Utilizadas
- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **SciPy**
- **Plotly**
- **Matplotlib**
- **Seaborn**
- **Plotnine**

## Funcionalidades
### 1. **Visualização do Dataset**
- Exibição das 5 primeiras linhas do dataset.
- Identificação das variáveis e sua classificação.

### 2. **Análise Estatística**
- Cálculo das medidas centrais e de dispersão.
- Interpretação dos quartis e distribuição das avaliações.

### 3. **Gráficos Interativos**
O dashboard permite selecionar diferentes tipos de análises:

#### a) **Distribuição de Poisson**
- Cálculo da distribuição de Poisson para modelagem de eventos raros.
- Exibição da fórmula e interpretação dos valores gerados.

#### b) **Análise de Polaridade**
- Gráfico de barras mostrando a distribuição das notas dadas pelos usuários.

#### c) **Distribuição Binomial**
- Modelagem da probabilidade de sucesso em um número fixo de tentativas.
- Gráfico interativo para variar os parâmetros e observar a distribuição resultante.

#### d) **Análise de Sentimento**
- Classifica os comentários entre "Positivos" e "Negativos" com base na nota atribuída.
- Gráfico de barras mostrando a quantidade de cada tipo de comentário.

## Estrutura do Projeto
|-- amazon_logo.webp

|-- amazon_reviews.csv

|-- app.py

|-- requirements.txt

|-- README.md

## Contribuição
- Se desejar contribuir para este projeto, fique à vontade para abrir um pull request com melhorias ou novas análises.

# Autor
Desenvolvido por Marcelo Vieira de Melo
