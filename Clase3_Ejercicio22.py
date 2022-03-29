from random import randint
def LlenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista

def LlenarAle(n):
    lista=[]
    num = randint(1,n)
    lista+=[num]
    for i in range(1,n):
        while num in lista:
            num = randint(1,n)
        lista+=[num]

    return lista
n=10
listaA= LlenarSec(n)
listaB= LlenarAle(n)

for i in range(len(listaA)):
    print("La persona:",listaA[i],"es pareja con:",listaB[i])