from automovil import Automovil
from automovilVolador import AutomovilVolador
from modulo.operacion import operacion

operacion.sumar(1,2)


#creacion de un automovil    
coche=Automovil("amarillo","Audi",50, 50)


coche.conducir()
coche.volar()


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

print (f"el automovil esta volando? {cocheVolador.esta_volando}")

cocheVolador.aterriza()

print (f"el automovil esta volando? {cocheVolador.esta_volando}")

cocheVolador.conducir()
cocheVolador.volar()
