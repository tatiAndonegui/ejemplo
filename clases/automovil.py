from clases.vehiculo import Vehiculo

class Automovil(Vehiculo): 
  ruedas=4 
  def __init__(self,color, marca, aceleracion, velocidad):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=velocidad

    #getters y setters

    def getColor(self):
      return self.color
    def getMarca(self):
      return self.marca
    def getAceleracion(self):
      return self.aceleracion
    def getVelocidad(self):
      return self.velocidad
    
    def setColor(self,color):
      self.color=color
    def setMarca(self,marca):
        self.marca = marca
    def setAceleracion(self,aceleracion):
      self.aceleracion = aceleracion
    def setVelocidad(self,velocidad):
      self.velocidad =velocidad

  #Metodos
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