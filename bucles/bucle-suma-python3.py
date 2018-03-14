#coding: utf8
#Carlos León

salir = "N"
numero = 1
maximo = 5
suma = 0

while (salir=="N"):
    if(numero%==2):
        print (numero ,)
        if(numero<=maximo-2):
            print ("+" ,)

        suma=suma+numero

    numero=numero+1

    if(numero > maximo):
        salir = "S"
print("=" , suma)
