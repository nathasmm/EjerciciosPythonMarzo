dias=int(input("Ingrese un numero de dias"))
anios= dias//365
meses=(dias%365)//30
semanas=(dias-(anios*365+meses*30))//7
dias=dias-(anios*365+meses*30+semanas*7)
print(dias,"Equivalen a",anios,"años",meses,"meses",anios,"años",semanas,"semanas y ",dias,"dias")