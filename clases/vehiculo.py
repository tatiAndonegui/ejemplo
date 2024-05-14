from clases.transporte import Transporte

class Vehiculo(Transporte):

    #creo anio como protected (1 guion) y modelo como privado (dos guiones)
    def __init__(self,anio,modelo,color, marca, aceleracion, velocidad):
        super().__init__(color, marca, aceleracion, velocidad)
        self._anio=anio
        self.__modelo=modelo

    
    #getters y setters

    def set_anio(self,nuevo_anio):
        self._anio=nuevo_anio
    def set_modelo(self,nuevo_modelo):
        self.__modelo=nuevo_modelo

    def get_modelo(self):
        return self.__modelo
    def get_anio(self):
        return self._anio

