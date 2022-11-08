#zoologo

Contador_edad1=0
contador_edad2=0
contador_edad3=0
from random import randint
animal=randint(0,10)

if animal == 1:
 n_animal=str('Elefante')
 cantidad_animal=20
elif animal ==2:
 n_animal=str('Jirafa')
 cantidad_animal=15
else:
 n_animal=str('chimpance')
 cantidad_animal=40

edad=randint(0,3) 

for edad in range(cantidad_animal):
    if edad<=3:
     Contador_edad1=Contador_edad1+1
    elif edad <=5:
     contador_edad2=contador_edad2+1
    else:
     contador_edad3=contador_edad3+1



print(f"El total de animales escogidos de mas de 5 años  son {contador_edad3} el porcentaje de edades es de {contador_edad3/cantidad_animal*100} %")
print(f"El total de animales ecogidos de 3 a 5 años son {contador_edad2} el porcentaje de edades es de {contador_edad2/cantidad_animal*100} %")
print(f"El total de animales escogidos de 1 a 3 años son {Contador_edad1} el porcentaje de edades es de {Contador_edad1/cantidad_animal*100} %")
print(f"La cantidad de {n_animal} a estudiar es {cantidad_animal}")




