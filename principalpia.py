# Librería para acceder a archivos CSV
import csv

# Librería para gestionar la entrada de los datos de la clase Contacto
import re

# Se importa la clase Contacto
from clasepia import Contacto 

# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter

# Se establece una función para borrar pantalla.
# Se usa, expresión lambda, que es equivalente a:
# def clear():
#   os.system('cls')
LimpiarPantalla = lambda: os.system('cls') #on Windows System

# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
# Retorna True si _txt cumple con el patrón definido en _regex
# Retrona False si no es así.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

# Expresiones regulares para cada campo.
NICKNAMERegEx="^[A-Z0-9]{5,15}$"
NOMBRERegEx="^[A-Z]+(([',. -][A-Z ])?[A-Z]*)*$"
CORREORegEs="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
TELEFONORegEx="^[0-9]{2} [0-9]{4} [0-9]{4}"
FECHANACIMIENTORegEx="^[0-9]{4}/[0-9]{2}/[0-9]{2}$"
GASTORegEx="^[-+]?\d*\.?\d*$"
entidadValida=True   


def principal():
    Contactos=[]
    while (True):
    LimpiarPantalla()
        print("LISTA DE CONTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Ordenamiento.
                Contactos.sort(key=attrgetter("NICKNAME""),reverse=False)
                # Barrido secuencial.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(contacto.NICKNAME)
                    print(contacto.NOMBRE)
                    print(contacto.CORREO)
                    print(contacto.TELEFONO)
                    print(contacto.FECHANACIMIENTO)
                    print(contacto.GASTO)   
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")
            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")


principal()
