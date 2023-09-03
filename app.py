import bd.base_datos as sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)




base_datos.crear_bd("pruebas1")


