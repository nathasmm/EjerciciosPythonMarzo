from random import randint
def Imprimir(tabla):
    for fila in tabla: #cada fila
        print("[",end="")
        for columna in fila: #cada columna en cada fila
            print("%3s"%columna,end="")
        print("]")

def Llenar(n):
    tabla=[]
    for i in range(n):
        tabla.append([])
        columnas=randint(1,10)
        for j in range(columnas):
            tabla[i]+=[randint(1,10)]
    return tabla

tabla=Llenar(10)
Imprimir(tabla)