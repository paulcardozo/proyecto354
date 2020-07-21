import threading as sh
dogo=1


def dos(datos):
    
    for a  in range(datos):
        print("hilo :", sh.currentThread().getName()," Identificador :", a)
        
    

hilos =[]
for b in range(50):
    hilo=sh.Thread(name=b,target=dos,args=(1000000000,))
    hilos.append(hilo)
for b in hilos:
    b.start()

for b in hilos:
    b.join()
    
    
print("termino todo")

