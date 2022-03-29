jornada=48
horasTrabajadas=49
pagoHora=2
pagoHoraExtra=3.5
if horasTrabajadas<=jornada:
    salario=horasTrabajadas*pagoHora
else:
    salario=(jornada*pagoHora)+((horasTrabajadas-jornada)*pagoHoraExtra)
print("Su pago total es de:",salario)