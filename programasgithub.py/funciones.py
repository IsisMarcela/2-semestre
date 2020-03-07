#PASS
# El codigo de la funcion es obligatorio. Si no hay 
# hay codigo por el momento puede correr al usar pass
def pendiente():
    pass

#VARIABLE GLOBAL:
# Si una variable se declara fuera de procedimiento 
variableglobal="Soy global"
# Dentro de las funciones, si se quiere usar la
# variable global, debe anteponerse la palabra
# reservada global
def norecibeargumentos():
    # Si se comenta la siguiente linea, usar la variable 
    # equivale a declarar una version local de la 
    # variable; si no se comenta, usar la variable 
    # implica usar la global 
    # global variableglobal
    variableglobal == 4
print("No recibe argumentos")
print(variableglobal)

#ARGUMENTO OPCIONAL:
# Es cuando le asignas un valor al momento de su declaracion.
# Siempre van al final de la lista de argumentos.
def argumentosopcionales(city = "Mty", country = "Mexico"):
    print("I am from " + city + ", " + country)

#RETURN
# La funcion retorna valores 
# Cuidar que el flujo del programa siempre los retorne.
# Se debe utilizar como expresion, atendiendo el 
# retorno correspondiente
def elevoalcuadrado(x):
  return x * x

def main():
    print(argumentosopcionales(city = "Mty", country = "Mexico"))
    print(elevoalcuadrado(4))
