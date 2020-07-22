

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
salida2=np.load("prueba_lema.npz") #  para las respuestas

salida3=np.load("prueba_lema_derivado.npz")# para el entrenamiento

# veamos como trabaja esa cosita

entrada="no funciona como debe por alguna razon "
#stop word

sf=stopwords.words('spanish') #importamos la libreria
aux=str(entrada).split(" ")
limpio=aux[:]
nueva_cadena=""
for a in aux:

    if a in sf:
        limpio.remove(a)
    else:
        nueva_cadena+=a+" "

#lematización 

nlp=spacy.load('es_core_news_sm')
deriva=SnowballStemmer(language='spanish')

aux2=nlp(str(nueva_cadena))
nueva_cadena=""
for token in aux2:
    deri=  deriva.stem(str(token.lemma_))
    nueva_cadena+=deri+ " "


sentencias.append("")

# ahora si lo incluimos al vector salida 3


fin=[]
for a in salida3["uno"]:
    print(a)
    fin.append(a)
print(nueva_cadena)
fin.append(nueva_cadena)


tfuno= tf()
tfdos=tfuno.fit_transform(raw_documents=fin)
validador=cs(tfdos[-1],tfdos)

idx=validador.argsort()[0][-2]
print("este es el idx",idx)

flat=validador.flatten()
flat.sort()
req_tfidf=flat[-2]
print(req_tfidf)

if(req_tfidf<=0.4):
    print("lo siento no puedo identicar que es lo que deseas")
else:
    if(entrada.__contains__("si")):

        sentencias.append(entrada)
        tfuno= tf()
        tfdos=tfuno.fit_transform(raw_documents=sentencias)
        validador=cs(tfdos[-1],tfdos)

        idx=validador.argsort()[0][-2]

    # se puede borrar tdo lo de arriba y cambiar sentencias por fin y con eso ya estaria funcionando como se debe 
        print("hola ",sentencias[idx])
    else:
        print("te falta mas dataset para que esto funcione de la forma correcta")

