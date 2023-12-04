import random

numTiradas = int(input("Número de tiradas: "))

if numTiradas <0:
    print("Error")
else:
    # JugadorA=[random.randint(1,6) for i in range(numTiradas)]
    # print(JugadorA)
    # maxResultadoJA=max(JugadorA)
    # minResultadoJA=min(JugadorA)
    # sumPuntosJA=maxResultadoJA+minResultadoJA
    # print(sumPuntosJA)
    #
    # JugadorB=[random.randint(1,6) for i in range(numTiradas)]
    # print(JugadorB)
    # maxResultadoJB=max(JugadorB)
    # minResultadoJB=min(JugadorB)
    # sumPuntosJB=maxResultadoJB+minResultadoJB
    # print(sumPuntosJB)
    #
    # if sumPuntosJA > sumPuntosJB:
    #     print("Jugador 1 gana!!")
    # elif sumPuntosJB > sumPuntosJA:
    #     print("Jugador 2 gana!!")
    # else:
    #     print("Empate!!")

    valorMin=7
    valorMax=0
    valorTotalJA=0
    valorTotalJB=0

    for i in range(numTiradas):
        numObtenido=random.randint(1,6)
        if numObtenido>valorMax:
            valorMax=numObtenido
        if numObtenido<valorMin:
            valorMin=numObtenido
        valorTotalJA=valorMin+valorMax
    print(f"valor maximo JA: {valorMax}")
    print(f"valor minimo JA: {valorMin}")
    print(f"total JA: {valorTotalJA}")

    for i in range(numTiradas):
        numObtenido = random.randint(1, 6)
        if numObtenido > valorMax:
            valorMax = numObtenido
        if numObtenido < valorMin:
            valorMin = numObtenido
        valorTotalJB = valorMin + valorMax
    print(f"valor maximo JB: {valorMax}")
    print(f"valor minimo JB: {valorMin}")
    print(f"total JB: {valorTotalJB}")

    if valorTotalJA>valorTotalJB:
        print("Jugador A gana")
    elif valorTotalJB>valorTotalJA:
        print("Jugador B gana")
    else:
        print("Empate")


longContraseñas=int(input("Ingrese la longitud de las contraseñas: "))
cadena="@$_ABCDEFRSTUVXYZghijklmnpq"
resultadoCadena=""
for i in range(longContraseñas):
    contContraseña = i + 1
    resultadoCadena += random.choice(cadena)
print(f"Contraseña {contContraseña}: {resultadoCadena}")