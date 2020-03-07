velocidad = 80
dinero = 500
precioAlto = float(input("Ingrese precio alto: "))
litrosDisp = (dinero/precioAlto)
rendimiento = float(input("Ingrese rendimiento:"))
distancia = (litrosDisp * rendimiento)
tiempo = (distancia/velocidad)
hora = round(tiempo,0)
minutoDecimal = (tiempo - hora)
minuto = (minutoDecimal * 60)

print("Recorrería " +str (distancia) + " km en " +str (hora) + " horas y " +str(minuto) + " minutos." )