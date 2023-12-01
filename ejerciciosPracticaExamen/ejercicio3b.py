import random

valorFinal=0
numTiradas=int(input("Ingrese el numero de tiradas: "))
if numTiradas<=0:
    print("El numero de tiradas no puede ser 0 o negativo")
else:
    for i in range(numTiradas):
        conTiradas=i+1
        numObtenido=random.randint(1,6)
        print(f"Tirada {conTiradas}, resultado: {numObtenido}")
        if numObtenido>valorFinal:
            valorFinal=numObtenido
    print(f"El numero mas alto obtenido es {valorFinal} ")