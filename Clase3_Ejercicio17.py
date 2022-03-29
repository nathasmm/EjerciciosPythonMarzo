saldo=0
op=0
while op!=3:
    op=int(input("Menú:\nIngrese una opción:\n1.-Depósito\n2.-Retiro\n3.-Salir\n"))
    if op>1 or op<4:
        if op==1:
            deposito= float(input("Ingrese la cantidad a depositar:"))
            saldo+=deposito
        elif op==2:
            retiro= float(input("Ingrese la cantidad a retirar:"))
            if retiro>saldo:
                print("No puede retirar esa cantidad de su cuenta")
            else:
                saldo-=retiro
        elif op==3:
            print("Su saldo es:",saldo,"\nSaliendo...")
    else:
        print("Opción no válida")