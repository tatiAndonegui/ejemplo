from automovil import Automovil
from automovilVolador import AutomovilVolador


#creacion de un automovil    
coche=Automovil("amarillo","Audi",50, 50)


#Muestro lo que el automovil puede hacer 
print(coche.ruedas)
print(coche.aceleracion)

coche.aceleracion=30
print(coche.aceleracion)

print (f"la aceleracion es de {coche.aceleracion}")

coche.acelera()

print (f"la velocidad despues de acelerar {coche.velocidad}")

coche.frena()

print (f"la velocidad despues de frenar {coche.velocidad}")


#creacion de un automovil Volador

cocheVolador=AutomovilVolador("gris","delorean",50, 50)

print (f"el automovil esta volando? {coche.esta_volando})