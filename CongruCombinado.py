__author__ = 'Talivaro'
xo1=int(input("Ingrese el valor de xo1: "))
xo2=int(input("Ingrese el valor de xo2: "))
xo3=int(input("Ingrese el valor de xo3: "))
repe=int(input("Numero de valores: "))
for i in range(repe):
    xn1=float((171*xo1)%30269)
    xn2=float((172*xo2)%30307)
    xn3=float((173*xo3)%30323)
    ui=float(((xn1/30269)+(xn2/30307)+(xn3/30323))%1)
    print(ui)
    xo1=xn1;
    xo2=xn2;
    xo3=xn3;
