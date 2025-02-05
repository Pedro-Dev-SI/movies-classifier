# Movies Classifier

Este projeto demonstra um pipeline completo de coleta, processamento e classificação de filmes. Ele consiste em:

- **Coleta de Dados:**  
  Extrai informações de filmes (título, sinopse e classificação etária) a partir da página dos Top 250 filmes do IMDb. Os dados são salvos em um arquivo JSON.

- **Treinamento de Modelo:**  
  Utiliza técnicas de processamento de linguagem natural (TF-IDF) para converter o texto dos filmes em features numéricas. Em seguida, aplica-se SMOTE para lidar com o desbalanceamento das classes e treina um modelo de regressão logística para classificar os filmes de acordo com a classificação etária (por exemplo: "Livre", "10", "12", "14", "16", "18").

- **Exposição dos Dados via API:**  
  O objetivo é criar uma API utilizando Flask para disponibilizar os dados e o modelo treinado. (Observação: A implementação da API pode ser expandida conforme necessário.)

## Estrutura do Projeto

- `web_scraping.py`  
  Script responsável por coletar os dados dos filmes a partir do IMDb e salvá-los em `movie_data.json`.

- `classifier.py`  
  Script que realiza o pré-processamento dos dados, treinamento e avaliação de um modelo de classificação. Também contém uma função para prever a classificação de novos filmes.

- `movie_data.json`  
  Arquivo gerado a partir do script de coleta, contendo os dados dos filmes.

- `requirements.txt`  
  Lista de dependências do projeto, que inclui:
  - requests
  - beautifulsoup4
  - scikit-learn
  - pandas
  - pymongo
  - flask

## Pré-requisitos

- Python 3.x
- Instale as dependências executando:
  ```bash
  pip install -r requirements.txt

## Como executar
    ```bash
    python web_scraping.py
    python classifier.py

## Melhorias

- Implementar uma API Rest utilizando Flask para consultar os dados dos filmes.
- Utilizar Mongo DB para armazenar os dados coletados.
- Aumentar a análise e o pré-processamento dos dados para melhorar a performance do modelo. 