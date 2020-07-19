import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la lematización



def limpiar(token,palabras):
    
    if token in palabras:
        palabras_limpia.remove(token)
        print("hilo :", th.currentThread().getName()," Identificador :", token)


w = open("salida.txt")
filtro=w.read()
sentencias=nk.sent_tokenize(filtro,'spanish')
#print(sentencias)
sf=stopwords.words('spanish')
palabras=nk.word_tokenize(filtro)
palabras_limpia=palabras[:]


hilos=[]

for tokens in palabras:

    hilos.append(th.Thread(name=tokens,target=limpiar,args=(tokens,sf,)))


for b  in hilos:
    b.start()
for b in hilos:
    b.join()

with open("salida_freq.txt",'w') as f:
        f.write(str(palabras_limpia))

np.savez_compressed('prueba.npz',uno=palabras_limpia)


#español=SnowballStemmer(language='spanish')
#print(español.stem("tiernito"))
freq=nk.FreqDist(palabras_limpia)

#for uno,dos in freq.items():
#    print(str(uno), " : ",str(dos))

freq.plot(20)

