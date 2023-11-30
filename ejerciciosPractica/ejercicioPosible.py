import random

numBuscado=int(input("Que numero has pensado? "))
numTiradas= int(input("Cuantos dados van a tirarse? "))

for dado in range(numTiradas):
    contTiradas=dado+1
    numObtenido=random.randint(1,6)
    print(f"Tirada {contTiradas}, resultado {numObtenido}")
    if numObtenido==numBuscado:
        print("ganaste, acertarste el numero!!")
        break
    else:
        print("Lo siento no se hacertó el numero...")