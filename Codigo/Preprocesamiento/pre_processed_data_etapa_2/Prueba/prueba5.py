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


# ahora se procede a hacer la lematización y derivacion regresiva de las oraciones
print("Iniciando con la lematización de las oraciones")

nlp=spacy.load('es_core_news_sm')
deriva=SnowballStemmer(language='spanish')
sentencias_reconstruidas=np.load("formu_oraciones.npz")

def lemmat(trabajo):
    
    aux3=""
   
    aux = nlp(str(trabajo))
    for token1 in aux:
        deri=  deriva.stem(str(token1.lemma_))
        aux3+=deri+ " "
    
    print(aux3)    
    cambiado_palabra.append(aux3)



hilos4=[]
cambiado_palabra = []



for tokens in sentencias_reconstruidas["uno"]:

    hilos4.append(th.Thread(name=tokens,target=lemmat,args=(tokens,)))


for b  in hilos4:
    b.start()
for b in hilos4:
    b.join()

np.savez_compressed('lemati_oraciones.npz',uno=cambiado_palabra)
print(cambiado_palabra)
print("Proceso de lematización, de las oraciones finalizado")
freq2=nk.FreqDist(np.load("lemati_palabras.npz")["uno"])
freq2.plot(20)
print("Proceso finalizado")


