class Registro:
  
    def __init__(self, temp:float, humedad:float, pAtms:float): #)constructor
     self.__temp = temp
     self.__humedad= humedad
     self.__pAtms= pAtms

    def getTemp(self):
        return (self.__temp)
    def gethumedad(self):
        return (self.__humedad)
    def getPresAtmosf(self):
        return(self.__pAtms)
    def __repr__(self):
        return f'{self.__temp}         {self.__humedad}         {self.__pAtms}'
    
    