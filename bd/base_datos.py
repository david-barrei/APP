import mysql.connector

acceso_bd = {"host": "localhost",
             "user": "root",
             "password": "root",
             "databases" : "app"}

class BaseDatos:
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)

    def consulta(self, sql):
        cursor = self.conector.cursor()
        cursor.execute(sql)
        return cursor
