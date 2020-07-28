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

def limpiar_stopwords_palabras(token,palabras):
    
    if token in palabras:
        palabras_limpia.remove(token)
        print("hilo :", th.currentThread().getName()," Identificador :", token)

print("Empezando con las stopword para las palabras")
w = open("salida.txt")
filtro=w.read()
sf=stopwords.words('spanish')
palabras=nk.word_tokenize(filtro)
palabras_limpia=palabras[:]


hilos=[]
for tokens in palabras:
    hilos.append(th.Thread(name=tokens,target=limpiar_stopwords_palabras,args=(tokens,sf,)))
for b  in hilos:
    b.start()
for b in hilos:
    b.join()

#Guardamos un vector con las stopwords ya procesadas

np.savez_compressed('stopwords_palabras.npz',uno=palabras_limpia)

print("Proceso de eliminiación de stopWord, de la palabras finalizado")

