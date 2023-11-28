# b) Escriba un programa que pida un número de dados, que tire el número de dados indicado y diga cuál es el valor más
# alto obtenido.

import random

numBuscado=0
numObtenido=0
conTiradas=0

numTiradas = int(input("Número de tiradas: "))

if numTiradas <= 0:
    print("El numero de tiradas no puede ser menor o igual a cero")

elif numTiradas > 5:
    print("El numero de tiradas no puede exceder de 5")

else:
    for i in range(numTiradas):
        contTiradas = i + 1
        numObtenido = random.randint(1, 6)
        print(f"Tirada {contTiradas}: {numObtenido}")

        if numObtenido > numBuscado:
            numBuscado = numObtenido
    print("El valor más alto es:", numBuscado)




