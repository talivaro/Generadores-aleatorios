__author__ = 'Talivaro'
xo=int(input("Ingrese x0: "))
val=int(input("Numero de valores: "))
for i in range(val):
    mod=0
    xn=5*xo+3
    mod =xn%16
    print ("x",i+1,mod)
    ui=float(mod/16)
    print ("U",i+1,ui)
    xo=mod
