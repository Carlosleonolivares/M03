# coding: utf8
# Carlos león olivares
# 12/03/2018

import os
os.system("clear")

salir = "N"
valor=1
maximo=5
suma=0
while ( salir=="N" ):
	
	print (valor)


	suma=suma+valor
	valor=valor+1
	
	if (valor>maximo):
    	    salir = "S"
            print (suma)
