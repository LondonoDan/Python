

valor_hora=float(input("Ingrese el valor de la hora de trabajo "))
horas=int(input("Ingrese las horas trabajadas en la semana "))

if horas >=56:
    extra_triple= horas -56
    valor_total= 48* valor_hora+(8* valor_hora *2)+(extra_triple*valor_hora*3)
elif horas >=48:
    extra_doble= horas -48
    valor_total = 48*valor_hora +(extra_doble*valor_hora*2)
else:
    valor_total= horas*valor_hora

print(f"El valor del pago por {horas} es de {valor_total}")

