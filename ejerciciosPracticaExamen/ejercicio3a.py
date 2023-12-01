import random
numTiradas=int(input("Ingrese el numero de tiradas: "))
if numTiradas<=0:
    print("El numero de tiradas no puede ser 0 o negativo")
else:
    numObjetivo=int(input("Ingrese el numero a obtener: "))
    if numObjetivo <1 and numObjetivo >6:
        print("El numero a conseguir tiene que ser entre 1 y 6")
    else:
        for i in range(numTiradas):
            conTirada=i+1
            numObtenido=random.randint(1,6)
            print(f"Tirada {conTirada}, resultado: {numObtenido}")
            if numObtenido==numObjetivo:
                print("Acertaste el numero")
                break
            else:
                print("No acertaste el numero")