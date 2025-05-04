import pandas as pd
import gensim
from gensim.models import Word2Vec
import os

# Verileri oku
df_lemma = pd.read_csv("lemmatized_output.csv")
df_stem = pd.read_csv("stemmed_output.csv")

# Tokenize edilmiş listeye dönüştür
def text_to_tokens(df_column):
    return [row.split() for row in df_column]

sentences_lemma = text_to_tokens(df_lemma["Lemmatized_Text"])
sentences_stem = text_to_tokens(df_stem["Stemmed_Text"])

# Parametre kombinasyonları
parameters = [
    {'model_type': 'cbow', 'window': 2, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 2, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 300},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 300},
]

# Klasör oluştur
os.makedirs("models", exist_ok=True)

# Model eğitme fonksiyonu
def train_models(sentences, label):
    for p in parameters:
        sg_val = 0 if p['model_type'] == 'cbow' else 1
        model = Word2Vec(
            sentences=sentences,
            vector_size=p['vector_size'],
            window=p['window'],
            sg=sg_val,
            min_count=1,
            workers=4,
            epochs=100
        )
        name = f"models/word2vec_{label}_{p['model_type']}_win{p['window']}_dim{p['vector_size']}.model"
        model.save(name)
        print(f"✅ Model kaydedildi: {name}")

# Model eğit
train_models(sentences_lemma, "lemmatized")
train_models(sentences_stem, "stemmed")
