import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la derivación regresiva
from nltk.stem import WordNetLemmatizer as wd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.metrics.pairwise import cosine_similarity as cs

#esta es una prueba para ver si tienes todo instalado para que funcione

# va ser separado primero se va a hacer el proceso de las palabras

#primer paso haceemos las stopwords



#ahora procedemos a hacer la lematización de las palabras 
print("Iniciando con la lematización de las palabras")
salida2=np.load("stopwords_palabras.npz")

#Con esto caragamos la libreria necesaria para hacer la lematización en español
nlp=spacy.load('es_core_news_sm')

def limpiar_lemati_palabras(trabajo):
    
    
        aux = nlp(str(trabajo))
        for token in aux:
            print(token, token.lemma, token.lemma_)
            cambiado.append(token.lemma_)
hilos2=[]
cambiado = []
for tokens in salida2['uno']:

    hilos2.append(th.Thread(name=tokens,target=limpiar_lemati_palabras,args=(tokens,)))
for b  in hilos2:
    b.start()
for b in hilos2:
    b.join()

#Guardamos la matriz lematizada

np.savez_compressed('lemati_palabras.npz',uno=cambiado)
print(cambiado)
print("Proceso de lematización, de la palabras finalizado")

