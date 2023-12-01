import random

numTiradasJ1=int(input("Ingrese el numero de tiradas: "))
if numTiradasJ1<=0:
    print("El numero de tiradas no puede ser 0 o negativo")
else:
    for i in range(numTiradasJ1):
        conTiradas=i+1
        numObtenidoJ1=random.randint(1,6)
        numObtenidoJ2 = random.randint(1, 6)
        print(f"Resultado tirada {conTiradas} jugador 1: {numObtenidoJ1}")
        print(f"Resultado tirada {conTiradas} jugador 2: {numObtenidoJ2}")

        if numObtenidoJ1 > numObtenidoJ2:
            print("El jugador 1 gana!")

        elif numObtenidoJ2 > numObtenidoJ1:
            print("El jugador 2 gana!")
        else:
            print("Empate!")
