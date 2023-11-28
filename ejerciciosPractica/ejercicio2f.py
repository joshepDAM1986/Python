# f) Escriba un programa que pida un número de dados y tire esa cantidad de dados para dos jugadores. El jugador que
# saque más puntos sumando su valor más alto y su valor más bajo, gana.

import  random



numTiradas = int(input("Número de tiradas: "))

if numTiradas <= 1 or numTiradas > 5:
    print("El número de tiradas debe estar entre 2 y 5.")
else:
    listaTiradasJ1=[random.randint(1,6) for i in range(numTiradas)]
    print(listaTiradasJ1)
    maxResultadoJ1=max(listaTiradasJ1)
    minResultadoJ1=min(listaTiradasJ1)
    sumPuntosJ1=maxResultadoJ1+minResultadoJ1
    print(sumPuntosJ1)

    listaTiradasJ2=[random.randint(1,6) for i in range(numTiradas)]
    print(listaTiradasJ2)
    maxResultadoJ2=max(listaTiradasJ2)
    minResultadoJ2=min(listaTiradasJ2)
    sumPuntosJ2=maxResultadoJ2+minResultadoJ2
    print(sumPuntosJ2)

    if sumPuntosJ1 > sumPuntosJ2:
        print("Jugador 1 gana!!")
    elif sumPuntosJ2 > sumPuntosJ1:
        print("Jugador 2 gana!!")
    else:
        print("Empate!!")

