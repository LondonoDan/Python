#validar cual de los dos buses es el que mas dinero recauda


bus1= str(input("Ingrese la placa del bus1 "))
pasajeros= int(input("Ingrese el total de pasajeros recogidos "))
valor_pasaje=float(input("Ingrese el valor del pasaje "))
totalbus1=valor_pasaje*pasajeros

bus2=str(input("Ingrese la placa del bus2 "))
pasajero=int(input("ingrese el total de pasajeros recogidos "))
valor_pasaje2=float(input("Ingrese el valor del pasaje "))
totalbus2=valor_pasaje2*pasajero

if totalbus1>totalbus2:
    print(f"el bus con placa {bus1} es el que mas dinero recaudo con un total de {totalbus1}")
else:
    print(f"el bus con placa {bus2} es el que mas dinero recaudo con un total de {totalbus2}")    
