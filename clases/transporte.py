from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,color, marca, aceleracion, velocidad):
        self.color=color
        self.marca=marca
        self.aceleracion=aceleracion
        self.velocidad=velocidad


    #getters y setters
    
    def set_color(self,color):
        self.color=color
    def set_marca(self,marca):
        self.marca = marca
    def set_aceleracion(self,aceleracion):
        self.aceleracion = aceleracion
    def set_velocidad(self,velocidad):
        self.velocidad =velocidad

    def get_color(self):
        return self.color
    def get_marca(self):
        return self.marca
    def get_aceleracion(self):
        return self.aceleracion
    def get_velocidad(self):
        return self.velocidad

#Metodos Abstractos   
    #@abstractmethod 
    #def volar(self):
        pass
    #def conducir(self):
        pass 

#Metodos
    def acelera(self):
        pass
    
    def frena(self):
        pass