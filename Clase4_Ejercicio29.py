dic={}

menu= True
def Imprimir(dic):
    for indice in dic:
        print("Producto:",indice,"Precio:",dic[indice])
while menu:
    op= int(input("Elija una opción\n1.-Agregar producto\n2.-Facturar\n3.Salir\n"))
    if op == 1:
        indice= input("Ingrese un indice: ")
        valor= float(input("Ingrese el valor: "))
        dic[indice]=valor
        print(dic)
    elif op==2:
        total=0
        factura=True
        Imprimir(dic)
        while factura:
            op=int(input("Ingrese una opcion:\n1.-Agregar a factura\n2.-Finalizar\n"))
            if op==1:
                indice= input("Ingrese un indice: ")
                cantidad= int(input("Ingrese la cantidad: "))
                if dic.get(indice) is None:
                    print("Producto no encontrado")
                else:
                    total += dic.get(indice)*cantidad
                    print("El total es",total)
            elif op==2:
                factura=False   
                total=0            
             
        

       
    elif op==3:
        menu=False
    else:
        print("Ingrese una opción válida")