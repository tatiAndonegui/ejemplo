from clases.vehiculo import Vehiculo

class Automovil(Vehiculo): 
  ruedas=4 
  def __init__(self,color, marca, aceleracion, velocidad,anio,modelo):
        super().__init__(color, marca, aceleracion, velocidad,anio,modelo,)
        

    
  #Metodos
  def conducir(self):
    return print ("estoy conduciendo")
  
  def volar(self):
    return print ("este vehiculo no vuela")

  def acelera(self):
    self.velocidad += self.aceleracion
    return print ("este vehiculo acelero a: ", str(self.velocidad)," km")
    
  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion
    return print ("este vehiculo despues de frenar se mantiene a la velocidad de: ", self.velocidad, " km")
  


