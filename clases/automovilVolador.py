from clases.automovil import Automovil


class AutomovilVolador(Automovil):
    ruedas = 6

    def __init__(self,color, marca, aceleracion, velocidad,esta_volando=True):
        super().__init__(color, marca, aceleracion, velocidad)

        self.esta_volando = esta_volando


    def conducir(self):
      return print ("estoy conduciendo")
  
    def volar(self):
      self.esta_volando=True
      return print ("este vehiculo vuela")

    def aterriza(self):
      self.esta_volando=False

