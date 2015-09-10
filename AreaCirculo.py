__author__ = 'Talivaro'
import math
import numpy as np
import matplotlib.pyplot as plt

val=int(input("Numero de valores: "))
def randux(ent):
    xo=101
    da1=[]
    for i in range(ent):
        mod =(17*xo+73)%487
        #print ("x",i+1,mod)
        ui=float(mod)/487
        #print ("U",i+1,ui)
        xo=mod
        da1.append(ui)
    return da1

def randuy(ent):
    xo=23
    da2=[]
    for i in range(ent):
        mod =(89*xo+19)%829
        #print ("x",i+1,mod)
        ui=float(mod)/829
        #print ("U",i+1,ui)
        xo=mod
        da2.append(ui)
    return da2

da1=randux(val)
da2=randuy(val)

c=0
N=val
sali=[]
plt.ion()
axi=plt.gca()

for i in range(val):
    da1[i]=(12)*da1[i]-6
    #print (da1)
for j in range(val):
    da2[j]=(12)*da2[j]-6
    #print (da2)

for i in range(val):
    #sali[i]=(da1[i]*da1[i])+(da2[i]*da2[i])
    if(6**2>=((da1[i]*da1[i])+(da2[i]*da2[i]))):#Esta dentro del circulo?
        c=c+1
        axi.plot(da1[i],da2[i],'g.')
        #print(sali,"1")
    else:
        #print(sali,"0")
        axi.plot(da1[i],da2[i],'r.')
    if i%70==0:
        plt.draw()
        plt.title("Area Teorica "+str(math.pi*25)+"Area Aproximada "+str((float(c)/val)*(100)))
acirculo=math.pi*25
aestimada=(float(c)/val)*(100)
errorRelPorcen=(abs(acirculo-aestimada)/acirculo)*100
print("Area Teorica:",math.pi*25,"Area estimada:", aestimada,"error: ",errorRelPorcen)
