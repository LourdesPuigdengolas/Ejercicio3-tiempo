from classRegistro import Registro 

def minYmax(registro_tiempo):
        minimo = None
        maximo = None
        for dia, registros in enumerate(registro_tiempo):
            for hora, registro in enumerate(registros):
                valor = registro.getTemp()
                if minimo is None or valor < minimo[0]:
                    minimo = (valor, dia+1, hora)
                if maximo is None or valor > maximo[0]:
                    maximo = (valor, dia+1, hora)
        print(f'El mínimo de temperatura el día {minimo[1]} a la hora {minimo[2]} es: {minimo[0]}')
        print(f'El máximo de temperatura el día {maximo[1]} a la hora {maximo[2]} es: {maximo[0]}')
    
        minimo = None
        maximo = None
        for dia, registros in enumerate(registro_tiempo):
            for hora, registro in enumerate(registros):
                valor = registro.gethumedad()
                if minimo is None or valor < minimo[0]:
                    minimo = (valor, dia+1, hora)
                if maximo is None or valor > maximo[0]:
                    maximo = (valor, dia+1, hora)
        print(f'El mínimo de humedad, día {minimo[1]} hora {minimo[2]}: {minimo[0]}')
        print(f'El máximo de humedad, día {maximo[1]} hora {maximo[2]}: {maximo[0]}')
    
        minimo = None
        maximo = None
        for dia, registros in enumerate(registro_tiempo):
            for hora, registro in enumerate(registros):
                valor = registro.getPresAtmosf()
                if minimo is None or valor < minimo[0]:
                    minimo = (valor, dia+1, hora)
                if maximo is None or valor > maximo[0]:
                    maximo = (valor, dia+1, hora)
        print(f'El mínimo de presion, el día {minimo[1]} hora {minimo[2]}: {minimo[0]}')
        print(f'El máximo de presion, el día {maximo[1]} hora {maximo[2]}: {maximo[0]}')
    
def promedioHora(registro_tiempo):
        for hora in range(24):
            valor = 0
            for dia in range(len(registro_tiempo)):
                valor += registro_tiempo[dia][hora].getTemp()
                prom= valor/len(registro_tiempo)
            print(f'La temperatura promedio a la hora {hora} es: {prom}') 
    
def listarDia(registro_tiempo,dia):
        registros = registro_tiempo[dia-1]
        print('Hora   Temperatura   Humedad   Presion')
        for hora, registro in enumerate(registros):
            print(f'{hora}       {repr(registro)}')