numero_secreto = int(input("Ingresa un número secreto: "))
inter = False
cont = 1
while not inter:
    num = int(input("Intente adivinar el número : "))
    if num > numero_secreto:
        cont+=1
        print ("El número es mayor")
    elif num < numero_secreto:
        cont+=1
        print ("El número es menor")
    else :
        inter = True
print("Número correcto! y has tardado " + str(cont) + " intentos" )