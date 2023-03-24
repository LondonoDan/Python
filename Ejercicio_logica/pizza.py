#Datos de entrada

print("   ¡BIENVENIDO A pizzería Bella Napoli!")
print("PIZZAS DISPONIBLES: Vegetariana (1) o No vegetariana (2)")
print("TODAS LAS PIZZAS VAN ACOMPAÑADAS DE Mozzarella Y Tomate")
pizzas = int (input("INGRESA LA OPCION DE LA PIZZA QUE DESEAS: "))



#Datatos de proceso - funcion

def pizzeria():
    if pizzas == 1:
        print("/////////////////////////////////////////////////")
        print(" LA PIZZA ESCOGIDA ES VEGETARIANA ")
        print("Ingredientes disponibles para la Pizza vegetariana son: Pimiento y Tofu. ")
        Ingredientes= int (input("Ingresa los ingredientes que deseas según el número ( Recuerda que solo puedes escoger 1 ingrediente) Pimiento (1) O Tofu (2) INGRESA LA OPCIÓN : "))

        if Ingredientes==1:
            print("La pizza escogida es Vegetariana con los ingredientes: Pimiento, Mozzarella y Tomate")
    
        elif Ingredientes ==2:
            print("La pizza escogida es Vegetariana con los ingredientes: Tofu, Mozzarella y Tomate")

        else:
            print("Ingrese un número valido. OPCIÓN 1 O 2")

    elif pizzas == 2:
        print("/////////////////////////////////////////////////")
        print(" lA PIZZA ESCOGIDA ES NO VEGETARIANA  ")
        print("Ingredientes disponibles para la Pizza no vegetariana son: Pepperoni, Jamon y salmón.")
        Ingredientes= int (input("Ingresa los ingredientes que deseas según el número ( Recuerda que solo puedes escoger 1 ingrediente) Pepperoni(1), Jamon(2) y Salmón(3) INGRESA LA OPCIÓN : "))
     

        if Ingredientes==1:
            print("La pizza escogida es  NO Vegetariana con los ingredientes: Pepperoni, Mozzarella y Tomate")

        elif Ingredientes ==2:
            print("La pizza escogida es NO Vegetariana con los ingredientes: Jamon, Mozzarella y Tomate")

        elif Ingredientes== 3:
            print("La pizza escogida es NO Vegetariana con los ingredientes: Salmón, Mozzarella y Tomate")    
        else:
            print("Ingrese un número valido. OPCION 1, 2 O 3")
    else:
         print("Ingrese un número valido. OPCIÓN 1 O 2")

pizzeria()
