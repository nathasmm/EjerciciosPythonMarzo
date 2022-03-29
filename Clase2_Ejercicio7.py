from random import randint  #Sintaxis de las importaciones en python
zonaUsuario =int(input("¿Qué zona desea disparar? "))
zonaPortero= randint(1,6) #aqui pongo el rango de los numeros, ese incluye el 1 y el 6
#randint(inicio, fin) numero aleatorio desde el inicio al fin tomando en cuenta los extremos
#random() sin parametros hace un numero aleatorio entre 0.0 y 1.0
#randrange(inicio,fin, paso) igual aleatorio entre inicio y fin con paso= que vaya de uno en uno, o de 2 en 2 en
#uniform(inicio,fin)genera un numero aleatorio de tipo flotante
print("La zona cubierta por el portero es",zonaPortero)
if zonaUsuario==zonaPortero:
    print("No ha sido un gol")
else:
    print("Goool")    
