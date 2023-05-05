from classRegistro import Registro 
import csv
from gestor import minYmax,promedioHora,listarDia


if __name__=='__main__':
    registro_tiempo = []

    with open("registro_tiempo.csv") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            #next(reader, None)      #Omitir el encabezado del archivo
            for fila in reader:
                dia = int(fila[0])
                hora = int(fila[1])
                temperatura = float(fila[2])
                humedad = float(fila[3])
                presion = float(fila[4])

                registro = Registro(temperatura, humedad, presion)
               
                if dia > len(registro_tiempo):
                    registro_tiempo.append([])
                registro_tiempo[dia-1].append(registro)


    print(f"--- MENU: ---")
    print(f"[1]. Mostrar para cada variable el día y hora de menor y mayor valor.")
    print(f"[2]. Mostrar la temperatura promedio mensual por cada hora.")
    print(f"[3]. Listar los valores de las tres variables para cada hora del día.")
    print(f"[0]. Salir")
    opcion= int(input("Ingrese el numero de opción que desea: "))
    while opcion != 0:
        if opcion == 1:
            minYmax(registro_tiempo)
        elif opcion == 2: 
            promedioHora(registro_tiempo)
        elif opcion == 3: 
            dia = int(input('Ingrese el dia a listar: '))
            listarDia(registro_tiempo,dia)
        else:
            print('Opcion invalida')
        opcion= int(input("Ingrese el numero de opción que desea: "))
                