import mysql.connector

acceso_bd = {"host": "localhost",
             "user": "root",
             "password": ""
             }

class BaseDatos:
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
    
    #Decorador para el reporte de base de datos
    def reporte_bd(funcion_parametro):
        def interno(self, nombre_bd):
            funcion_parametro(self, nombre_bd)
            print("Estas son las bases de datos creadas\n")
            BaseDatos.mostrar_bd(self)
        return interno

    def consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    #muestra la base de datos del servidor
    def mostrar_bd(self):
        self.cursor.execute("SHOW DATABASES")
        for bd in self.cursor:
            print(bd)

    #eliminar una base de datos
    @reporte_bd
    def eliminar_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}")
            print(f"Se elimino correctamente {nombre_bd}")
        except:
            print(f"Base de datos {nombre_bd} no encontrada\n")
           
    @reporte_bd
    def crear_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}")
            print(f" Se creo la base de datos {nombre_bd}")
        except:
            print(f"Ocurrio un error ")


