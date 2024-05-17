from clases.vehiculo import Vehiculo
from clases.automovil import Automovil
from clases.automovilVolador import AutomovilVolador
from modulo.operacion import operacion
import sqlite3



#creacion de un automovil    
#coche=Automovil("amarillo","Audi",50,50,2023,"A1")
#print(f"El coche tiene {coche.ruedas} ruedas y una aceleración de {coche.aceleracion}")
#Modificamos la acelaracion y mostrar en pantalla ambas acelaraciones
#coche.aceleracion  = 20
#print(f"El coche tiene una aceleración {coche.aceleracion} km")
#Acelero el coche
#coche.acelera()
#coche.volar()

#creacion de un automovil 2
#coche2=Automovil("verde","Renault",10, 20,1969,"12")
#coche2.acelera()
#print (coche2.aceleracion)
#coche.conducir()
#coche.volar()

#coche3=Automovil("rojo","audi",20,60,2000,"r1")
#coche3.datos()
#coche3.acelera()
#print (coche3.aceleracion)
#print (coche3.velocidad)
#coche3.datos()

#Muestro lo que el automovil puede hacer 
#print(coche.ruedas)
#print(coche.aceleracion)

#coche.aceleracion=30
#print(coche.aceleracion)

#coche.frena()


#creacion de un automovil Volador

#cocheVolador=AutomovilVolador("gris","delorean",50, 50, 1970,"doc")
#cocheVolador.datos()

#print (f"el automovil esta volando? {cocheVolador.esta_volando}")

#cocheVolador.aterriza()

#print (f"el automovil esta volando? {cocheVolador.esta_volando}")

#cocheVolador.conducir()
#cocheVolador.volar()


#creo un vehiculo
#vehiculo1=Vehiculo("azul","chevrolet",10, 70, 2004,"corsa")
#vehiculo1.datos()
#print(vehiculo1._anio)
#vehiculo1._anio=2022

#print(vehiculo1._anio)



#creo la suma
#operacion.sumar(1,2)
#print (f"la suma entre ambos numeros es {operacion.sumar}")

#Sqlite3
print("conecto a mi base de datos")
conexion=sqlite3.connect("base_datos/mi_base.bd")
cursor=conexion.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculo(id INTEGER PRIMARY KEY AUTOINCREMENT,color TEXT, marca TEXT, aceleracion INTEGER,velocidad INTEGER, anio INTEGER,modelo TEXT)''')
#conexion.commit()
vehiculo1=Vehiculo("azul","chevrolet",10, 70, 2004,"corsa")
cursor.execute('''INSERT INTO vehiculo (color,marca,aceleracion,velocidad,anio,modelo) VALUES(?,?,?,?,?,?)''',
            (vehiculo1.get_color(), vehiculo1.get_marca(),vehiculo1.get_aceleracion(), vehiculo1.get_velocidad(),vehiculo1.get_anio(),vehiculo1.get_modelo()))

cursor.execute('''SELECT * FROM vehiculo''')
resultados=cursor.fetchall()

for file in resultados:
    print (file)

cursor.close()
conexion.close()

