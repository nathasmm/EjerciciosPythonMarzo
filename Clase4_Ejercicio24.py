def LlenarSecuencia(n):
    tabla=[]
    contador=0
    for i in range(n):
        tabla.append([]) #Este método nos permite agregar nuevos elementos a una lista
        for j in range(n):
            contador=contador+1
            tabla[i]+=[contador]
    return tabla

def Imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print("]")

Imprimir (LlenarSecuencia(5))