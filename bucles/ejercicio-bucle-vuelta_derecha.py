#coding: utf8
#Carlos León Olivares
#15/03/2018

contador=1
maximo=8
salir="N"

while(salir=="N"):
    if(contador%8==1 or contador%8==2):
        print (contador ,"- Arriba")
    if(contador%8==3 or contador%8==4):
        print (contador ,"- Derecha")
    if(contador%8==5 or contador%8==6):
        print (contador ,"- Abajo")
    if(contador%8==7 or contador%8==0):
        print (contador ,"- Izquierda")
    contador=contador+1
    if(contador > maximo):
        salir = "S"