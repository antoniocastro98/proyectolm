from lxml import etree
from Funciones import listar, contar, buscar, informacion, libre
datos=etree.parse("archivoxml.xml")


print(''' MENU
1.Listar información: Mostrar el nombre de las canales de los que tenemos información.

2.Contar información: Mostrar la cantidad de canales que son de deportes.

3.Buscar o filtrar información: Pedir por teclado el nombre de un canal y mostramos la programación.

4.Buscar información relacionada: introducir el nombre de un programa y mostrar el canal donde se emite.

5.Ejercicio libre: Introducir un idioma y mostrar los canales.''')

opcion=int(input("Introduce una opción: "))

while opcion<0 or opcion>5:
    print ("Error, introduce una opción correcta")
    opcion=int(input("Introduce una opción: "))

while opcion!=0:
    if opcion==1:
        
        for i in listar(datos):
            print (i)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==2:
        contador=len(contar(datos))
        for i in contar(datos):
            print (i)
        print ("El número de programas de deportes es: " ,contador)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==3:
        lista3=[]
        canal=input("Introduce el canal que quieres buscar: ")
        for i in buscar(datos,canal):
            print(i)
            lista3.append(i)
        if len(lista3)==0:
            print("El canal",canal," no existe o no tiene programación")
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==4:
        lista4=[]
        programa=input("Introduce el nombre del programa que quieres buscar(Pon un espacio al final del nombre): ")
        for i in informacion(datos,programa):
            print(i)
            lista4.append(i)
        if len(lista4)==0:
            print("El programa",programa," no existe o no está en la programación")
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==5:
        idioma=input("Introduce el idioma (es o en) que quieres buscar: ")
       
        for i in libre(datos,idioma):
            print(i)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))


if opcion==0:
    print("Fin del programa")