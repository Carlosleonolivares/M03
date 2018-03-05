#coding: utf8

salir="N"
valor1=1
valor2=input("Hasta que numero quieres contar? ")


while(salir=="N"):
	print "Número",valor1
	
	
	if (valor1 > valor2) or (valor<=0):
		salir = "S"
valor1 = valor1 +1
