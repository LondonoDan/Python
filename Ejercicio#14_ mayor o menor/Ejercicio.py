#ejercicio #14 verificar que número es mayor y menor

nombre1= input( "Ingrese su nombre")
nombre2= input( "Ingrese su nombre")
edad1= int (input ("Ingrese su edad"))
edad2= int(input("Ingrese su edad "))
if edad1==edad2:
    print(f"{nombre1} y {nombre2} tienen la misma edad {edad1}")
elif edad1>edad2:
    print(f"{nombre1} es el mayor con {edad1} años ")
else:
    print(f"{nombre2} es el menor con {edad2} años ")
