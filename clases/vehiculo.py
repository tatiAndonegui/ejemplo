from abc import ABC, abstractmethod

class Vehiculo(ABC):

    #creo anio como protected (1 guion) y modelo como privado (dos guiones)
    def __init__(self,anio,modelo):
        self._anio=anio
        self.__modelo=modelo

    @abstractmethod 
    def volar(self):
        pass
    def conducir(self):
        pass   
    
