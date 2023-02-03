array = [1 , 2, 3, 4, 5]

for num in array :
    cont = 0
    while cont <= 10:
        mult = cont * num
        print( str(num) + " * " + str(cont) + " = " + str(mult) )
        cont += 1
    print("Final")

