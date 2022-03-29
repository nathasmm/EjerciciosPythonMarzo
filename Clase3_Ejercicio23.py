listaPersonas=[80,34,80,23,70]
suma=0
pesoMax=listaPersonas[0]
for i in range(len(listaPersonas)):
   for j in range(i+1,len(listaPersonas)):
      suma= listaPersonas[i]+listaPersonas[j]
      if suma<=150:
         print("La suma de: ",listaPersonas[i] ,"+", listaPersonas[j]," = ",suma)
         if suma>pesoMax:
            pesoMax = suma
print("El peso maximo posible es:",pesoMax)

      

