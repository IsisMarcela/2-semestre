# Programa que lea archivos CSV, y lo carga en un objeto, y lo almacena en una lista.

# Librería para acceder a archivos CSV
import csv


# Clase para almacenar los contactos
class Contacto:
      def __init__(self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANACIMIENTO,GASTOS):
            self.NICKNAME = NICKNAME
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO
            self.TELEFONO = TELEFONO
            self.FECHANACIMIENTO = FECHANACIMIENTO
            self.GASTOS = GASTOS

  
# Lectura secuencial del archivo
with open('contactos_mobil.csv') as csvarchivo:
  entrada = csv.reader(csvarchivo)
  for reg in entrada:
    print(reg)  # Cada línea se muestra como una lista de campos   
