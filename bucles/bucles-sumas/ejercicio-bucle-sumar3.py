#coding: utf8
#Carlos León
#19/03/2018

salir = "N"
numero=1
maximo=5
suma=0
while ( salir=="N" ):
    print (numero ,)
    if(numero<=maximo-1):
        print ("+" ,)
	
    suma=suma+numero
    numero=numero+1

    if ( numero > maximo ): 
            salir = "S"
print ("=" , suma) 