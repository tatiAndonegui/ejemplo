from clases.automovil import Automovil


class AutomovilVolador(Automovil):
    ruedas = 6
    def __init__(self,color, marca, aceleracion, velocidad,anio,modelo,esta_volando=True):
        super().__init__(color, marca, aceleracion, velocidad,anio,modelo,)
        self.esta_volando = esta_volando

    #getters y setters--CORREGIR COMO EN VEHICULO

    def getEsta_volando(self):
      return self.esta_volando
    def setEsta_volando(self,esta_volando):
      self.esta_volando=esta_volando


    #Metodos
    def conducir(self):
      return print ("estoy conduciendo")
  
    def volar(self):
      self.esta_volando=True
      return print ("este vehiculo vuela")

    def aterriza(self):
      self.esta_volando=False
      return print ("este vehiculo ha aterrizado")
    

    #Imprime los datos del automovil
    def datos(self):
      print("Las ruedas del automovil volador son", self.ruedas)

