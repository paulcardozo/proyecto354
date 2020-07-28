

import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la derivación regresiva
from nltk.stem import WordNetLemmatizer as wd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.metrics.pairwise import cosine_similarity as cs



salida2=np.load("formu_oraciones.npz") #  para las respuestas

salida3=np.load("lemati_oraciones.npz")# para el entrenamiento

sentencias=[]
for a in salida2["uno"]:
    sentencias.append(a)

fin=[]
for a in salida3["uno"]:
    #print(a)
    fin.append(a)

# ingresamos al bucle de consulta

while(True):
    entrada=input("Introduce alguna consulta : ")


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
    print(nueva_cadena)
    fin.append(nueva_cadena)

    #hacemos la transformación
    tfuno= tf()
    tfdos=tfuno.fit_transform(raw_documents=fin)
    validador=cs(tfdos[-1],tfdos)
    
    #buscamos la aproximación 
    idx=validador.argsort()[0][-2]
    print("este es el idx",idx)

    flat=validador.flatten()
    flat.sort()
    req_tfidf=flat[-2]
    print(req_tfidf)

    if(req_tfidf<=0.7):
        print("lo siento no puedo identicar que es lo que deseas")
    else:
        if(nueva_cadena.__contains__("hac") or nueva_cadena.__contains__("pod")):
            sentencias.append(entrada)
            tfuno= tf()
            tfdos=tfuno.fit_transform(raw_documents=sentencias)
            validador=cs(tfdos[-1],tfdos)
            idx=validador.argsort()[0][-2]

    
            print("Cadena Comparada : ",sentencias[idx])
            print("Se puede decir  que se necesita de asistencia tecnica")
        else:
            if nueva_cadena.__contains__("si"):
                print("Se puede decir que se solicita información")
            else:    
                print("Lo siento no puedo identificar que es lo que deseas")



