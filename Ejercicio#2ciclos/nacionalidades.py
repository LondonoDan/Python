#validar el tipo de nacionalidad

n=70
contador_colaltos=0
contador_colbajos=0
contador_colmedios=0
contador_arg_altos=0
contador_arg_medios=0
contador_arg_bajos=0
contador_brasil_altos=0
contador_brasil_medios=0
contador_brasil_bajos=0
Contador_colombianos=0
contador_argentinos=0
contador_brasil=0
contador_mayor=0
contador_menor=0
for i  in range(n):
      print("---ciclo "+str(i+1)+"---")
    
      nacionalidad=int(input("Ingrese la nacionalidad Colombiano(1), Argentino(2), brasileño(3) "))
      edad=int(input("Ingrese la edad "))
      tipo=int(input("Ingrese el tipo Alto (1), Bajo(2), Medio(3)"))

      if nacionalidad == 1 and tipo == 1:
       contador_colaltos=contador_colaltos+1
     
      elif nacionalidad ==1 and tipo ==2:
       contador_colbajos= contador_colbajos+1

      if nacionalidad ==1 and tipo ==3:
       contador_colmedios= contador_colmedios+1

      elif nacionalidad ==2 and tipo ==1:
       contador_arg_altos=contador_arg_altos+1

      if nacionalidad ==2 and tipo == 2:
       contador_arg_bajos=contador_arg_bajos+1

      elif nacionalidad ==2 and tipo ==3:
       contador_arg_medios= contador_arg_medios+1

      if nacionalidad ==3 and tipo ==1:
       contador_brasil_altos=contador_brasil_altos+1   

      elif nacionalidad==3 and tipo ==2:
       contador_arg_bajos= contador_brasil_bajos+1

      if nacionalidad==3 and tipo ==3:
       contador_brasil_medios=contador_brasil_medios+1

      elif nacionalidad==1:
       Contador_colombianos=Contador_colombianos+1

      if nacionalidad==2:
       contador_argentinos=contador_argentinos+1    

      elif nacionalidad ==3:
       contador_brasil= contador_brasil+1

      if edad >=18:
       contador_mayor=contador_mayor+1
      else:
       contador_menor=contador_menor+1

print(f"Los colombianos altos son {contador_colaltos}")
print(f"Los colombianos bajos son {contador_colbajos}")
print(f"Los colombianos medios son {contador_colmedios}")

print(f"Los Argentinos altos son {contador_arg_altos}")
print(f"Los Argentinos bajos son {contador_arg_bajos}")
print(f"Los Argentinos medios son {contador_arg_medios}")

print(f"Los Portugueses altos son {contador_arg_altos}")
print(f"Los Portugueses bajos son {contador_arg_bajos}")
print(f"Los Portugueses medios son {contador_arg_medios}")

print(f"El total de Colombianos en los registros son {Contador_colombianos}")
print(f"El total de Argentinos en los registros son {contador_argentinos}")
print(f"El total de Portugueses en los registros son {contador_brasil}")
print(f"La cantidad de personas Mayores de edad son {contador_mayor}")
print(f"La cantidad de personas Menores de edad son {contador_menor}")

