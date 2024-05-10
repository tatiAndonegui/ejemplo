from clases.vehiculo import Vehiculo

class Automovil(Vehiculo): 
  ruedas=4 
  def __init__(self,color, marca, aceleracion, velocidad):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=velocidad

    #getters y setters

    def get_color(self):
      return self.color
    def get_marca(self):
      return self.marca
    def get_aceleracion(self):
      return self.aceleracion
    def get_velocidad(self):
      return self.velocidad
    
    def set_color(self,color):
      self.color=color
    def set_marca(self,marca):
        self.marca = marca
    def set_aceleracion(self,aceleracion):
      self.aceleracion = aceleracion
    def set_velocidad(self,velocidad):
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