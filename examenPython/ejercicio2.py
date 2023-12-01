import  random

numTiradas = int(input("Número de tiradas: "))

if numTiradas <0:
    print("Error")
else:
    JugadorA=[random.randint(1,6) for i in range(numTiradas)]
    print(JugadorA)
    maxResultadoJ1=max(JugadorA)
    minResultadoJ1=min(JugadorA)
    sumPuntosJ1=maxResultadoJ1+minResultadoJ1
    print(sumPuntosJ1)

    JugadorB=[random.randint(1,6) for i in range(numTiradas)]
    print(JugadorB)
    maxResultadoJ2=max(JugadorB)
    minResultadoJ2=min(JugadorB)
    sumPuntosJ2=maxResultadoJ2+minResultadoJ2
    print(sumPuntosJ2)

    if sumPuntosJ1 > sumPuntosJ2:
        print("Jugador 1 gana!!")
    elif sumPuntosJ2 > sumPuntosJ1:
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