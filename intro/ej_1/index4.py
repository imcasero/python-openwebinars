num1 = float(input("Introduzca el  numero 1 :"))
num2 = float(input("Introduzca el  numero 2 :"))

if num1 > num2:
    rest = num1 - num2
    suma = num2 + num1
    mult = num2 * num1
    div = num1 / num2
else :
    rest = num2 - num1
    suma = num2 + num1
    mult = num2 * num1
    div = num2 / num1

print("Rest = " + str(rest) + "/ div = " + str(div) + "/ suma = " + str(suma) + "/ mult = " + str(mult))