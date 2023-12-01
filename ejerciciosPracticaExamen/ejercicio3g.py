import random

numAnterior=0

numTiradas=int(input("Ingrese el numero de tiradas: "))
if numTiradas<=0:
    print("El numero de tiradas no puede ser menor o igual a 0")
else:
    for i in range(numTiradas):
        conTiradas=i+1
        numObtenido=random.randint(1,6)
        print(f"Tirada {conTiradas}, resultado {numObtenido}")

        if numObtenido==numAnterior:
            print("Perdiste, salieron dos dados iguales seguidos")
            break
        numAnterior=numObtenido
    else:
        print("Ganaste, no salieron dos dados iguales seguidos")

