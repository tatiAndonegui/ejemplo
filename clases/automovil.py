from clases.vehiculo import Vehiculo

class Automovil(Vehiculo): 
  ruedas=4 
  def __init__(self,color, marca, aceleracion, velocidad):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=velocidad

  def conducir(self):
    return print ("estoy conduciendo")
  
  def volar(self):
    return print ("este vehiculo no vuela")

  def acelera(self):
    self.velocidad=self.velocidad+self.aceleracion
    return print ("este vehiculo acelero a: ", self.velocidad," km")
    

  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion
    return print ("este vehiculo despues de frenar se mantiene a la velocidad de: ", self.velocidad, " km")