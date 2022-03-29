from random import randint
aciertos=0

v= True
while v:
    op=randint(1,2)
    num1= randint(1,10)
    num2= randint(1,10)
    if op==1:
        res=num1*num2
        print(num1,"*",num2,"=")
        resUsuario= int(input("Ingrese la respuesta a la operacion: "))
        if resUsuario==res:
            aciertos+=1
            print("Respuesta correcta")
            v= True
        else:
            print("Incorrecto la respuesta correcta era",res)
            v= False
    elif op==2:
        res=num1//num2
        print(num1,"/",num2,"=")
        resUsuario= int(input("Ingrese la respuesta a la operacion: "))
        if resUsuario==res:
            aciertos+=1
            print("Respuesta correcta")
            v= True
        else:
            print("Incorrecto la respuesta correcta era",res)
            v= False
print("Tuvo un total de",aciertos,"respuestas correctas")