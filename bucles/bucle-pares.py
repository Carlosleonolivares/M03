#coding: utf8
#Carlos León

salir="N"
valor1=2
valor2=input("Hasta que numero quieres contar? ")

if(valor2<=1):
	salir = "S"
else:
	while(salir=="N"):
		print "Número",valor1
			
		valor1 = valor1 +2
			
		if (valor1 > valor2) or (valor2<=1) :
			salir = "S"
