# validar el pago de un trabajador segun el contrato 

trabajador= str(input("Ingrese el tipo de trabajador Temporal o Fijo "))

if trabajador == 'TEMPORAL' or trabajador == 'Temporal':
    nombre=str(input("Ingrese el nombre del trabajador ")) 
    n_Horas=int(input("Ingrese el número de horas trabajadas "))
    salario_neto=n_Horas*6000
    print(f"El total del pago del trabajador {nombre} es de {salario_neto} número de horas trabajadas {n_Horas}")
elif trabajador == 'FIJO' or trabajador == 'Fijo':
     nombre=str(input("Ingrese el nombre del trabajador ")) 
     n_horas=int(input("Ingrese el número de horas trabajadas "))
     deducciones=float(input("Ingrese el total de deducciones "))
     bonificacion=float(input("Ingrese la bonificación"))
     salario_neto=n_horas*6000
     salario_final=salario_neto+bonificacion-deducciones
     print(f"El total del pago del trabajador {nombre} por horas trabajadas y valor de la hora es de {salario_neto}")
     print(f"El total de la bonificación es de {bonificacion}")
     print(f"El total de las deducciones es de {deducciones}")
     print(f"El salario neto contando bonificación y deducciones es de {salario_final}")
else:
    print("Respuesta invalida intentelo de nuevo")
     