anioInicio= 1900
anioFin=2022
r="Los años bisiestos entre "+str(anioInicio)+" y "+str(anioFin)+" son: "
for i in range(anioInicio,anioFin+1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        r=r +str(i)+" , "
print(r)
