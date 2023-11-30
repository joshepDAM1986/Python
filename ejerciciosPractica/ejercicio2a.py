# EJERCICIO 2:
# Programar los siguientes mini-juegos de dados (random). No es necesario usar listas y debéis controlar los errores
# asociados a valores incorrectos (numero de jugadores negativo, un dado es de 6 caras, etc):

# a) Escriba un programa que pida un número de dados, que pida un valor a conseguir y que tire después el número de
# dados indicado. El jugador gana si saca el valor ganador.

import random
bucle = True

while bucle:
    numTiradas = int(input("Número de tiradas (1-5): "))

    if numTiradas <=0 or numTiradas >5:
        print("El numero de tiradas debe estar entre 1 y 5")
    else:
        numBuscado = int(input("Número a conseguir (1-6): "))
        if numBuscado <1 or numBuscado >6:
            print("El numero buscado deber estar entre 1 y 6")
        else:
            for i in range(numTiradas):
                contTiradas = i+1
                numObtenido = random.randint(1, 6)
                print(f"Resultado de tirada {contTiradas}: {numObtenido}")

                if numObtenido == numBuscado:
                    print("¡Nais!")
                    bucle= False
                    break
                elif contTiradas < numTiradas:
                    print("No, inténtalo de nuevo!!")
                    bucle = False
                else:
                    print("No adivinaste el número...")
                    bucle = False
                    break


