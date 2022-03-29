frase= input("Ingrese una frase: ")
letra= input("Ingrese una letra: ")
contador=0

for carac in frase:
    if carac==letra:
        contador+=1

if contador!=0:
    print("La letra",letra,"se encontro",contador,"veces en la frase",frase)
else:
    print("La letra",letra,"no se encuentra en la frase",frase)