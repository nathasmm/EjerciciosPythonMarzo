lista = [1,"hola",3.5,False]
while len(lista)>0: #Mientras la longitud de la lista sea mayor q 0
    print(lista)
    elem=int(input("Ingrese la posicion del elemento a eliminar: "))
    if elem>len(lista)-1:
        print("\nEl elemento está fuera del rango")
        continue
    del(lista[elem])
    print()
