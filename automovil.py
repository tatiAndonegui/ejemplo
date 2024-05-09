class Automovil: #clase Automovil
  ruedas=4 #atributos de la clase
  def __init__(self,color, marca, aceleracion, velocidad):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=velocidad

  def acelera(self):
    self.velocidad=self.velocidad+self.aceleracion

  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion