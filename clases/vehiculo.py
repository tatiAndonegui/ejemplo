from clases.transporte import Transporte

class Vehiculo(Transporte):

    #creo anio como protected (1 guion) y modelo como privado (dos guiones)
    def __init__(self,color, marca, aceleracion, velocidad,anio,modelo,):
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

#Imprime informaciòn del automovil
    def info(self):
        print(self.color)
        print(self.marca)
        print(self.aceleracion)
        print(self.velocidad)
        print(self._anio)
        print(self.__modelo)
    