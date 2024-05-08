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
    
coche=Automovil("amarillo","Audi",50, 50)

print(coche.ruedas)
print(coche.aceleracion)

coche.aceleracion=30
print(coche.aceleracion)

print (f"la aceleracion es de {coche.aceleracion}")

coche.acelera()

print (f"la velocidad despues de acelerar {coche.velocidad}")

coche.frena()

print (f"la velocidad despues de frenar {coche.velocidad}")
