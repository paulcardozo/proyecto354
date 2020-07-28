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


#Ahora se procede a hacer para las oraciones

# este lu usaremos para las palabras entonces en primra instancia
# formaremos oraciones incluyendo puntos al final de cada linea

print("inicio de formulación de oraciones")

w = open("salida.txt")
filtro=w.read()# ahora debemos remplazar cada salto de linea con .
filtro=filtro.replace("\n",". ")
# en este punto se procede a formar el nuevto vector de palabras
sentencias=nk.sent_tokenize(filtro)
# una vez realizada la tokenización procedemos a cambiar el . por espacios nulos.
for a in range(len(sentencias)):
    sentencias[a]=sentencias[a].replace(".","")
# ahora procedemos a quitar las stopword

np.savez_compressed('formu_oraciones.npz',uno=sentencias)
print(sentencias)

print("Proceso de formulacion  de las oraciones finalizado")

# se procede a realizar la limpieza de las stopwords 

