print("pepe pecas pica papas con un pico pica papas pepe pecas")
frase= str.split("pepe pecas pica papas con un pico pica papas pepe pecas")
def contar_palabras ():
    palabra= (input("Ingrese la palabra a contar de la frase anterior: "))
    contar=0
    for i in frase: 
        if(palabra==i):
            contar+=1
    print("la palabra ", palabra, "se repite ", contar,"veces")
contar_palabras()