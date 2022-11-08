#validar si un estudiante gana la materia segun la cantidad de notas sacando el promedio de ellas

nombre=str(input("Ingrese el nombre del estudiante "))
nota1=float(input("Ingrese la primer nota "))
nota2=float(input("Ingrese la segunda nota "))
nota3=float(input("Ingrese la tercer  nota "))
nota4=float(input("Ingrese la cuarta nota "))
nota_final=(nota1+nota2+nota3+nota4)/4

if nota_final<3.0:
    print(f"El estudiante {nombre} PIERDE la materia nota final de {nota_final}")
elif nota_final <4.0:
       print(f"El estudiante {nombre} HABILITA la materia nota final de {nota_final}") 
else:
    print(f"El estudiante {nombre} GANA la materia nota final de {nota_final}") 