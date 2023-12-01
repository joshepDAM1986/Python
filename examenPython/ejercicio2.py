import random

numTiradas = int(input("Número de tiradas: "))

if numTiradas <0:
    print("Error")
else:
    JugadorA=[random.randint(1,6) for i in range(numTiradas)]
    print(JugadorA)
    maxResultadoJA=max(JugadorA)
    minResultadoJA=min(JugadorA)
    sumPuntosJA=maxResultadoJA+minResultadoJA
    print(sumPuntosJA)

    JugadorB=[random.randint(1,6) for i in range(numTiradas)]
    print(JugadorB)
    maxResultadoJB=max(JugadorB)
    minResultadoJB=min(JugadorB)
    sumPuntosJB=maxResultadoJB+minResultadoJB
    print(sumPuntosJB)

    if sumPuntosJA > sumPuntosJB:
        print("Jugador 1 gana!!")
    elif sumPuntosJB > sumPuntosJA:
        print("Jugador 2 gana!!")
    else:
        print("Empate!!")


longContraseñas=int(input("Ingrese la longitud de las contraseñas: "))
cadena="@$_ABCDEFRSTUVXYZghijklmnpq"
resultadoCadena=""
for i in range(longContraseñas):
    contContraseña = i + 1
    resultadoCadena += random.choice(cadena)
print(f"Contraseña {contContraseña}: {resultadoCadena}")