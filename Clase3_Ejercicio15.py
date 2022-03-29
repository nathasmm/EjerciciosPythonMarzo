
def vasos(n,x): #asi definimos un metodo, no es necesario especificar el return, a lo largo del metodo veo si retornno o no
    total=0
    while n>=x:
        reciclados=n//x
        sobrantes= n%x
        total+=reciclados # comp pongo un operador de asignacion debo inicializarle
        n=reciclados+sobrantes
        print("N:",n,"Reciclados:",reciclados,"sobran:",sobrantes,"total reciclados",total)

n=60
x=8
vasos(n,x)


