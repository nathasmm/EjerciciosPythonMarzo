lista= [1,3,5,7,1,8,5]
for i in range((len(lista)-1),-1,-1): #recorrer el arreglo al revés 
    if lista[i] in lista[:i]:
        del(lista[i])
print(lista)    
