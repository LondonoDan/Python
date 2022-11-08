#Validar si una persona es apta para ingresar a un equipo segun caractristicas sexo, edad,peso,estatura

sexo=str(input("Ingrese el sexo de la persona Femenino (F) o Masculino (M) "))
edad=int(input("Ingrese la edad "))
estatura=float(input("Ingrese la estatura "))
peso=float(input("Ingrese el peso "))

if sexo != 'f' or sexo != 'F' and sexo != 'M' or sexo != 'm':
    print(f"la información ingresada no es correcta ingrese de nuevo")
elif sexo == 'f' or sexo == 'F' and edad >=18 and peso <=75 and estatura <=1.70:
    print(f"ES APTA PARA INGRESAR AL EQUIPO")
elif sexo == 'm' or sexo == 'M' and edad >=16 and peso <=60 and estatura <=1.70:
    print(f"ES APTO PARA INGRESAR AL EQUIPO")
else:
    print(f"NO ES APTO PARA INGRESAR AL EQUIPO")
