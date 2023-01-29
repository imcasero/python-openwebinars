minutes_total = int(input("Introduzca un numero de minutos"))

if minutes_total < 60:
    print("Ha introducido " + str(minutes_total) + " minutos")
else :
    minutos = minutes_total % 60
    horas = minutes_total // 60#las dos barras son division entera
    print("Minutos " + str(minutos) + " horas " + str(horas))