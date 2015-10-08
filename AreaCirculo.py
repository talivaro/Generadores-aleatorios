__author__ = 'Talivaro'

import math
import numpy as np
import matplotlib.pyplot as plt

val=int(input("Numero de valores: "))
def randux(ent):
    xo=101
    da1=[]
    for i in range(ent):
        mod =(17*xo+73)%127
        #print ("x",i+1,mod)
        ui=float(mod)/127
        #print ("U",i+1,ui)
        xo=mod
        da1.append(ui)
    return da1

def randuy(ent):
    xo=23
    da2=[]
    for i in range(ent):
        mod =(41*xo+19)%269
        #print ("x",i+1,mod)
        ui=float(mod)/269
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
        d=1/(N*100)
        d=d+d
        axi.plot(da1[i],da2[i],'g.')
        #print(sali,"1")
    else:
        #print(sali,"0")
        axi.plot(da1[i],da2[i],'r.')
    if i%120==0:
        plt.draw()
        plt.title("Area del circulo"+str(math.pi*25))

aestimada=c*d
print("Area Teorica:",math.pi*25, aestimada,c)
