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

dprint("Empezando con las stopword para las oraciones")

sf=stopwords.words('spanish') #importamos la libreria
sentencias=np.load("formu_oraciones.npz")
sentencias_reconstruidas=[] # aca llenaremos lo que queremos 
#definimos la funcion para limpiar de las stopword
def limpiar_stopwords_oraciones(token,palabras):

    aux= str( token).split(" ")#generamos la matriz
    rec=""
    print("hilo :", th.currentThread().getName()," Identificador :", token)
    for a in aux:
        if a in palabras:
            aux.remove(a)
        else:
            rec+=a+" "
    sentencias_reconstruidas.append(rec)


hilos3=[]

for tokens in sentencias["uno"]:

    hilos3.append(th.Thread(name=tokens,target=limpiar_stopwords_oraciones,args=(tokens,sf,)))


for b  in hilos3:
    b.start()
for b in hilos3:
    b.join()

np.savez_compressed('stopword_oraciones.npz',uno=sentencias_reconstruidas)
print(sentencias_reconstruidas)

print("Proceso de eliminiación de stopWord, de la oraciones finalizado")





