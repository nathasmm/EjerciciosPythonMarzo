dic={}
indice= "nombre"
valor= "kira"
dic.setdefault(indice,valor)
print(dic)

menu= True
while menu:
    op= int(input("Elija una opción\n1.-Agregar\n2.-Salir\n"))
    if op == 1:
        indice= input("Ingrese un indice: ")
        valor= input("Ingrese el valor: ")
        dic[indice]=valor
        print(dic)
    elif op==2:
        menu=False
    else:
        print("Ingrese una opción válida")