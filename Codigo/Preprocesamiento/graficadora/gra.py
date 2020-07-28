import nltk as nk
import numpy as np
import threading as th
from nltk.corpus import stopwords # con eseto vamos a realizar el preprocesamiento eliminao stopwords
from nltk.stem import SnowballStemmer # con este vamos a hacer la derivación regresiva
from nltk.stem import WordNetLemmatizer as wd
import spacy


#w = open("salida.txt")
#filtro=w.read()
#sentencias=nk.word_tokenize(filtro,'spanish')

salida2=np.load("lemati_palabras.npz")

freq=nk.FreqDist(salida2['uno'])
#print(sentencias)
#freq=nk.FreqDist(sentencias)
freq.plot(20)