from abc import ABC, abstractmethod

class Vehiculo(ABC):

    #creo anio como protected (1 guion) y modelo como privado (dos guiones)
    def __init__(self,anio,modelo):
        self._anio=anio
        self.__modelo=modelo

    
    #getters y setters

    def get_anio(self):
        return self._anio
    def set_anio(self,nuevo_anio):
        self._anio=nuevo_anio

    def get_modelo(self):
        return self.__modelo
    def set_anio(self,nuevo_modelo):
        self.__modelo=nuevo_modelo

    @abstractmethod 
    def volar(self):
        pass
    def conducir(self):
        pass   
    

