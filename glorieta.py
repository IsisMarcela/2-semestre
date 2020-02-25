diametro = float(input("Ingrese diametro de la glorieta: "))
pi = 3.14
perimetro = (pi * diametro)
precioMetro = float(input("Ingrese el precio por metro: "))
precioMalla = (perimetro * precioMetro)
print("El precio total seria: " +str(precioMalla))