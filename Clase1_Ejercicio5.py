correctos = int(input("Ingrese el numero de aciertos: "))
incorrectos = int(input("Ingrese el numero de errores: "))
totalPreg=correctos+incorrectos
porcentajeCorrecto=(100/totalPreg)*correctos
porcentajeIncorrecto=(100/totalPreg)*incorrectos
print("Su puntaje final fue:",correctos,"/",totalPreg)
print("Su porcentaje de aciertos es: %.2f  y su porcentaje de errores es: %.2f "%(porcentajeCorrecto,porcentajeIncorrecto))