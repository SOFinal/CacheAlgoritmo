#!/usr/bin/python
import sys
import time

print sys.argv
global frame

cache = {}
orden = {}
contador=0
tamano = int(sys.argv[3])
pageF = 0

principal = []



cachelru = []


ordenlru = []

def optimo():
	global char, pageF, temp, i, contadorOp
	if len(principal)< tamano:
		if not [char,0] in principal:
			principal.append([char,0])
			pageF += 1
		lista.remove(char) 
		return
	else:
		if not [char,0] in principal:
			pageF += 1
			indice = lista.index(char)
            #i = indice
			contadorOp = 0
			while indice < len(lista)-1:
				indice+=1
				temp = lista[indice]
				if [temp,0] in principal:
					principal.remove([temp,0])
					principal.append([temp,1])
					contadorOp+=1
					if contadorOp==tamano-1:
						indice=len(lista)
			principal[0][0]=char
                    
			j=1
			for j in range(tamano):
				principal[j][1]=0
		lista.remove(char)
	return
	
def lru():
    global pageF,frame
    if len(cachelru)< tamano:
        if not frame in cachelru:
            cachelru.append(frame)
            ordenlru.append(frame)
            pageF += 1
        else:
            ordenlru.remove(frame)
            ordenlru.append(frame)
        return
    else:
        if not frame in cachelru:
            menosusado = ordenlru[0]
            indice = cachelru.index(menosusado)
            cachelru.insert(indice, frame)
            cachelru.remove(menosusado)
            ordenlru.remove(menosusado)
            ordenlru.append(frame)
            pageF += 1
        else:
            ordenlru.remove(frame)
            ordenlru.append(frame)
    return
	
def clock():
    global frame, pageF
    contarInde=0
    contarInde2=0
    if len(principal)< tamano:
        for i in range(len(principal)):
			
            if not frame==principal[i][1]:
                contarInde+= 1
            else:
                principal[i][2]=1
        if len(principal)==0:
                principal.append([1, frame, 0])
                pageF += 1
        if contarInde ==(len(principal)  ):
            principal.append([0, frame, 0])
            pageF += 1
        return
    else:
         for j in range(tamano):
            if  frame==principal[j][1]:
                principal[j][2]=1
            else:
                contarInde2+= 1
         j=0
         if contarInde2==tamano:
             while j < tamano:
                    if principal[j][0]==1 :
                        if principal[j][2]==0:
                            if j+1>=(tamano):
                                principal[0][0]=1
                            else:
                                principal[j+1][0]=1
                            principal[j][1]=frame
                            principal[j][0]=0
                            principal[j][2]=0
                            pageF += 1
                            j=tamano
                        else:
                            if principal[j][2]==1:
                                principal[j][2]=0
                                principal[j][0]=0
                                if j+1>=(tamano):
                                    principal[0][0]=1
                                    j=-1
                                else:
                                    principal[j+1][0]=1
                    j+= 1
    return


				
def lfu():
    global frame, pageF ,contador
		
    if len(cache)< tamano:
        if not frame in cache:
			contador += 1
			cache[frame]=1
			orden[frame]=contador
			pageF += 1
			
        else:
			contador += 1
			cache[frame]+=1
			orden[frame]=contador
	return
        
    else:
        if not frame in cache:
			contador += 1
		
			menosReferenciado,ignored = min(cache.iteritems(), key=lambda x:x[1])
			del cache[menosReferenciado]
			
			
			cache[frame]=1
			
			pageF += 1
            
        else:
			contador += 1
			cache[frame]+=1
			
			
    return

inicio=0
fin=0
inicio = time.time()
print "Recorriendo archivo..."
with open(sys.argv[1], "r") as ins:
        
		 
		if sys.argv[2]=='lfu':
			for frame in ins:
				frame = frame.rstrip('\n')
				
				lfu()
		if sys.argv[2]=='lru':
			for frame in ins:
				frame = frame.rstrip('\n')
				contador += 1
				lru()
		if sys.argv[2]=='optimo':
			#with open(sys.argv[1], "r") as ins:
			
			lista = ins.readlines()
			maximo = len(lista)
			contador=maximo
			z=0
			
			while z < maximo:
				char = lista[0]
				optimo()
				z+=1
		if sys.argv[2]=='clock':
			for frame in ins:
				contador += 1
				frame = frame.rstrip('\n')
				clock()
                
                
            


        



print "Page faults: ",pageF


ins.close()

fin = time.time()
total = fin - inicio

missRate=(pageF*1.00/contador*1.00)*100
missRateW=(pageF*1.00/(contador-tamano)*1.00)*100
print "TIEMPO: ",total," segundos"


print "Miss rate:     ",missRate,"% (W misses out of ",contador," references)"

print "Miss rate (warm cache):   ",missRateW,"% (W misses out of ",contador," - ",tamano," references) "
print 


