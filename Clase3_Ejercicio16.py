from random import randint
from time import gmtime

ganadas=0

def ppt(op):
    if op==1:
        r="Piedra"
    elif op==2:
        r="Papel"
    else:
        r="Tijera"
    return r

gMaquina=0
while ganadas<3 and gMaquina<3:
    opUsuario=int(input("Ingrese una opción:\n1.Piedra\n2.-Papel\n3.-Tijera\n"))
    if opUsuario>3 or opUsuario<1:
        print("Ingrese una opción valida")
        continue #Este hace que las intrucciones de abajo no se hagan
    opMaquina= randint(1,3)
    print("Usted eligió:",ppt(opUsuario))
    print("La máquina eligió:",ppt(opMaquina))
    if (opUsuario==1 and opMaquina==3) or (opUsuario==3 and opMaquina==2) or(opUsuario==2 and opMaquina==1):
        print("Gana el usuario")
        ganadas+=1
    elif opUsuario==opMaquina:
        print("Es un empate")
    else:
        gMaquina+=1
        print("Gana la máquina")
    print("Ganadas Usuario:",ganadas)
    print("Ganadas Máquina:",gMaquina)
    print()
    
