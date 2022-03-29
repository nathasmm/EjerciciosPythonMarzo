lista1=["h","k","a","g","s"]
lista2=["k","m","h","g","b"]
listaTodo=[]
lSoloPrimera=[]
lSoloSegunda=[]
lAmbas=[]
listaTodo=lista1+lista2
for palabra in lista1: #foreach
    if palabra in lista2: 
        lAmbas+=[palabra]
    else: 
        lSoloPrimera+=[palabra]  

for palabra in lista2: 
    if palabra not in lAmbas: 
        lSoloSegunda+=[palabra]
print("Lista 1")
print(lista1)
print("Lista 2")
print(lista2)
print("Ambas")
print(lAmbas)
print("Solo la primera")
print(lSoloPrimera)
print("Solo la segunda")
print(lSoloSegunda)
