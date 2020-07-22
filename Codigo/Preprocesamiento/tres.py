import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la derivación regresiva
from nltk.stem import WordNetLemmatizer as wd
import spacy

#este programa va servir para hacer el analisis y reconocimiento 

w=open("salida_freq.txt")
salida2=np.load("prueba.npz")


nlp=spacy.load('es_core_news_sm')

def limpiar(trabajo):
    
    
        aux = nlp(str(trabajo))
        for token in aux:
            print(token, token.lemma, token.lemma_)
            cambiado.append(token.lemma_)



hilos=[]
cambiado = []


for tokens in salida2['uno']:

    hilos.append(th.Thread(name=tokens,target=limpiar,args=(tokens,)))


for b  in hilos:
    b.start()
for b in hilos:
    b.join()



#for a in salida2['uno']:
#    aux=nlp(str(a))
#    for token in aux:
#        print(token, token.lemma, token.lemma_)
#        cambiado.append(token.lemma_)


#print(salida2['uno'].tolist())

#np.savez_compressed('prueba_lema.npz',uno=cambiado)
freq=nk.FreqDist(salida2['uno'])

freq.plot(20)

freq=nk.FreqDist(cambiado)

freq.plot(20)
