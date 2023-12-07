import random

numTiradas = int(input("Número de tiradas: "))

if numTiradas < 0:
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

    valorMinA = None
    valorMaxA = None
    valorMinB = None
    valorMaxB = None
    valorTotalJA = 0
    valorTotalJB = 0

    for i in range(numTiradas):
        conTirada= i+1
        numObtenido = random.randint(1, 6)
        if valorMaxA == None:
            valorMaxA = numObtenido
        if numObtenido > valorMaxA:
            valorMaxA = numObtenido
        if valorMinA == None:
            valorMinA = numObtenido
        if numObtenido < valorMinA:
            valorMinA = numObtenido
        valorTotalJA = valorMinA + valorMaxA
        print(f"Numeros tirada {conTirada} : {numObtenido}")
    print(f"valor maximo JA: {valorMaxA}")
    print(f"valor minimo JA: {valorMinA}")
    print(f"total JA: {valorTotalJA}")

    for j in range(numTiradas):
        conTirada = j + 1
        numObtenido = random.randint(1, 6)
        if valorMaxB == None:
            valorMaxB = numObtenido
        if numObtenido > valorMaxB:
            valorMaxB = numObtenido
        if valorMinB == None:
            valorMinB = numObtenido
        if numObtenido < valorMinB:
            valorMinB = numObtenido
        valorTotalJB = valorMinB + valorMaxB
        print(f"Numeros tirada {conTirada}: {numObtenido}")
    print(f"valor maximo JB: {valorMaxB}")
    print(f"valor minimo JB: {valorMinB}")
    print(f"total JB: {valorTotalJB}")

    if valorTotalJA > valorTotalJB:
        print("Jugador A gana")
    elif valorTotalJB > valorTotalJA:
        print("Jugador B gana")
    else:
        print("Empate")

longContraseñas = int(input("Ingrese la longitud de las contraseñas: "))
cadena = "@$_ABCDEFRSTUVXYZghijklmnpq"
resultadoCadena = ""
for i in range(longContraseñas):
    contContraseña = i + 1
    resultadoCadena += random.choice(cadena)
print(f"Contraseña {contContraseña}: {resultadoCadena}")
