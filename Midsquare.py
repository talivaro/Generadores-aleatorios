if __name__ == "__main__":
    xo=str(input("Ingrese el valor de la semilla: "))
    n=int(len(xo)/2)
    if len(xo)%2==0:
        repe=int(input("Numero de valores: "))
        for i in range(repe):
            d=len(xo)
            cero=""
            xo=int(xo)
            xo2=xo*xo
            y=str(xo2)
            for j in range((4*n)-len(y)):
                cero+="0"
            y=cero+y
            print(y)
            xo=str(xo)
            y2=y[int((2*d)/4):int((2*d*3)/4)]
            print("x",(i+1),y2)
            salida=y2
            xo=salida
            i=i+1
    else:
        print("Numero de digitos no par")
