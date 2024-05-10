from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod 
    def volar(self):
        pass
    def conducir(self):
        pass   
    
