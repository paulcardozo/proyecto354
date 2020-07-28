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

print("Empezando con las stopword para las oraciones")

sf=stopwords.words('spanish') #importamos la libreria

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

for tokens in sentencias:

    hilos3.append(th.Thread(name=tokens,target=limpiar_stopwords_oraciones,args=(tokens,sf,)))


for b  in hilos3:
    b.start()
for b in hilos3:
    b.join()

np.savez_compressed('stopword_oraciones.npz',uno=sentencias_reconstruidas)
print(sentencias_reconstruidas)

print("Proceso de eliminiación de stopWord, de la oraciones finalizado")


# ahora se procede a hacer la lematización y derivacion regresiva de las oraciones
print("Iniciando con la lematización de las oraciones")

nlp=spacy.load('es_core_news_sm')
deriva=SnowballStemmer(language='spanish')


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



for tokens in sentencias_reconstruidas:

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






