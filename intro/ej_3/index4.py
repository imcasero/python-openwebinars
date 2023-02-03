num = int(input("Introduzca un numero para comprobar si es primo :"))

primo = True
for i in range(2 , num):
    if num%i == 0:
        primo = False
        break

if primo:
    print("Este numero es primo!")
else:
    print("Este numero NO es primo!")