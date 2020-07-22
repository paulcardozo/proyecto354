

import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la derivación regresiva
from nltk.stem import WordNetLemmatizer as wd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.metrics.pairwise import cosine_similarity as cs


# este lu usaremos para las palabras entonces en primra instancia
# formaremos oraciones incluyendo puntos al final de cada linea
w = open("salida.txt")
filtro=w.read()# ahora debemos remplazar cada salto de linea con .
filtro=filtro.replace("\n",". ")
# en este punto se procede a formar el nuevto vector de palabras
sentencias=nk.sent_tokenize(filtro)
# una vez realizada la tokenización procedemos a cambiar el . por espacios nulos.
for a in range(len(sentencias)):
    sentencias[a]=sentencias[a].replace(".","")

print(sentencias)
salida2=np.load("prueba_lema.npz")

# veamos como trabaja esa cosita
dogo=[]
dogo=salida2["uno"][:]

sentencias.append("xiaomi es mejor que oppo")








tfuno= tf()
tfdos=tfuno.fit_transform( raw_documents=sentencias)
validador=cs(tfdos[-1],tfdos)
idx=validador.argsort()[0][-2]
flat=validador.flatten()
flat.sort()
req_tfidf=flat[-2]
print(req_tfidf)

if(req_tfidf==0):
    print("lo siento no puedo identicar que es lo que deseas")
else:
    print("hola ",sentencias[idx])


