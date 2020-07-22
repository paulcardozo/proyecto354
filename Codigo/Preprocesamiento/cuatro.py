import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la derivación regresiva
from nltk.stem import WordNetLemmatizer as wd
import spacy


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
# ahora procedemos a quitar las stopword
sf=stopwords.words('spanish') #importamos la libreria

sentencias_reconstruidas=[] # aca llenaremos lo que queremos 
#definimos la funcion para limpiar de las stopword
def limpiar(token,palabras):

    aux= str( token).split(" ")#generamos la matriz
    rec=""
    print("hilo :", th.currentThread().getName()," Identificador :", token)
    for a in aux:
        if a in palabras:
            aux.remove(a)
        else:
            rec+=a+" "
    sentencias_reconstruidas.append(rec)

    #for a in token:
        #if token in palabras:
            #sentencias_limpias.remove(token)
            
            #print("hilo :", th.currentThread().getName()," Identificador :", token)

#ejecuatamos la limpieza

hilos=[]

for tokens in sentencias:

    hilos.append(th.Thread(name=tokens,target=limpiar,args=(tokens,sf,)))


for b  in hilos:
    b.start()
for b in hilos:
    b.join()

#una vez eliminado las stopword se procede a hacer la lematización


#w=open("salida_freq.txt")
#salida2=np.load("prueba.npz")


nlp=spacy.load('es_core_news_sm')
deriva=SnowballStemmer(language='spanish')


def lemmat(trabajo):
    
    aux3=""
   
    aux = nlp(str(trabajo))
    for token1 in aux:
        #print(token1, token1.lemma, token1.lemma_,deriva.stem(str(token1.lemma_)))
        deri=  deriva.stem(str(token1.lemma_))
        
        #aux2+=str(token1.lemma_)+" "
        aux3+=deri+ " "
    
    print(aux3)    
    cambiado.append(aux3)



hilos2=[]
cambiado = []



for tokens in sentencias_reconstruidas:

    hilos2.append(th.Thread(name=tokens,target=lemmat,args=(tokens,)))


for b  in hilos2:
    b.start()
for b in hilos2:
    b.join()

np.savez_compressed('prueba_lema_derivado.npz',uno=cambiado)
print(cambiado)

#ya teniendo todo lematizado se procede a manejar los 

#print(sentencias_reconstruidas)
#print(filtro)