import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import numpy as np

# Carregar os dados do JSON
with open('movie_data.json', 'r') as file:
    data = json.load(file)

# Transformar os dados em um DataFrame
df = pd.DataFrame(data)

# Mapeando as classificações para números
classification_map = {
    "Livre": 0,
    "10": 1,
    "12": 2,
    "14": 3,
    "16": 4,
    "18": 5
}
df['classification'] = df['classification'].map(classification_map)

# Remover valores ausentes em 'classification'
print(f"Valores ausentes em y antes do tratamento: {df['classification'].isna().sum()}")
df = df.dropna(subset=['classification'])
print(f"Valores ausentes em y após o tratamento: {df['classification'].isna().sum()}")

# Combinar título e plot
X = df['title'] + ' ' + df['plot']
y = df['classification'].astype(int)

# Transformar texto em representação numérica com TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
X_tfidf = tfidf.fit_transform(X)

# Tratar classes desbalanceadas com SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_tfidf, y)

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Criar o pipeline com TF-IDF e Logistic Regression
pipeline = Pipeline([
    ('model', LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42))
])

# Treinar o modelo
pipeline.fit(X_train, y_train)

# Fazer previsões
y_pred = pipeline.predict(X_test)

# Avaliar o modelo
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=classification_map.keys()))

# Função para prever classificação de um novo filme
def predict_classification(title, plot):
    movie_description = title + ' ' + plot
    movie_tfidf = tfidf.transform([movie_description])
    prediction = pipeline.predict(movie_tfidf)
    class_name = [key for key, value in classification_map.items() if value == prediction[0]]
    return class_name[0]

# Teste da função
new_movie_title = "The Magical Forest Adventure"
new_movie_plot = "A group of curious children stumble upon a magical forest where they meet talking animals and mythical creatures. Together, they embark on a quest to find a lost treasure and save the enchanted land."
print("Predicted Classification:", predict_classification(new_movie_title, new_movie_plot))
