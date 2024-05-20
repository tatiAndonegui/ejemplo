import sqlite3

class Conexion:
    def __init__(self,nombre_bd):
        self.conexion=sqlite3.connect(nombre_bd)
        self.cursor=self.conexion.cursor()
    
    def crear_tabla_vehiculos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculo(id INTEGER PRIMARY KEY AUTOINCREMENT,color TEXT, marca TEXT, aceleracion INTEGER,velocidad INTEGER, anio INTEGER,modelo TEXT)''')
        self.conexion.commit()
    
    def insertar_vehiculo(self,vehiculo):
        self.cursor.execute('''INSERT INTO vehiculo (color,marca,aceleracion,velocidad,anio,modelo) VALUES(?,?,?,?,?,?)''',
        (vehiculo.get_color(), vehiculo.get_marca(),vehiculo.get_aceleracion(), vehiculo.get_velocidad(),vehiculo.get_anio(),vehiculo.get_modelo()))

        self.conexion.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()