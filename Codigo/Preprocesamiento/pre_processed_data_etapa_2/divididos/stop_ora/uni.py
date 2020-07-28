import nltk as nk
import numpy as np
import threading as th
# con esto vamos a realizar el preprocesamiento eliminando stopwords
from nltk.corpus import stopwords
# con este vamos a hacer la derivación regresiva
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer as wd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.metrics.pairwise import cosine_similarity as cs

reco = []
salida2 = np.load("1.npz")
for a in salida2["uno"]:
    reco.append(a)
salida2 = np.load("2.npz")
for a in salida2["uno"]:
    reco.append(a)
salida2 = np.load("3.npz")
for a in salida2["uno"]:
    reco.append(a)
#salida2 = np.load("formu_oraciones.npz")
#for a in salida2["uno"]:
#    reco.append(a)
#salida2 = np.load("5.npz")
#for a in salida2["uno"]:
#    reco.append(a)
#salida2 = np.load("6.npz")
#for a in salida2["uno"]:
#    reco.append(a)

np.savez_compressed('stopword_oraciones.npz',uno=reco)
print(reco)
