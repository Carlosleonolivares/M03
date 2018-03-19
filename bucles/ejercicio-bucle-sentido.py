#coding: utf8
#Carlos León Olivares
#15/03/2018

contador=1
maximo=8
sentido=input("Hacia que sentido quieres girar?  "
              "D --> Derecha   I --> Izquierda ")
sentido=sentido.upper()
salir="N"
if(sentido=="D") or (sentido=="I"):
    while(salir=="N"):
        if(contador%8==1 or contador%8==2):
            print (contador ,"- Arriba")
        if(contador%8==3 or contador%8==4):
            if(sentido=="D"):
                print (contador ,"- Derecha")
            else:
                print (contador ,"- Izquierda")
        if(contador%8==5 or contador%8==6):
            print (contador ,"- Abajo")
        if(contador%8==7 or contador%8==0):
            if(sentido=="D"):
                print (contador ,"- Izquierda")
            else:
                print (contador ,"- Derecha")
        contador=contador+1
        if(contador > maximo):
            salir = "S"
else:
    print ("Porfavor seleciona izquierda o derecha.")