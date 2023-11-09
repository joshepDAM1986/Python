import random

# EJERCICIO 9
# Escribir un programa que pida un número float y calcule su
# potencia de exponente entero que también se pide por teclado
# Si alguna entrada de datos no es incorrecta mostrar un mensaje
# de error

# numFloat=input("Introduzca un float: ")
# numEntero=input("Introduce el numero entero: ")
#
# if(numEntero.isnumeric() and numFloat.replace(".","",1).isnumeric()):
#     numFloat=float(numFloat)
#     numEntero=int(numEntero)
#     resultado= round(numFloat**numEntero,2)
#     print(f"El resultado es {resultado}")


# EJERCICIO 10
# Escribir un programa que simule el juego de piedra, papel,
# tijera en la que existen dos jugadores (Ana y Juan) Ambos
# representados por la máquina generando valores aleatorios de
# manera que el valor 1 corresponda a piedra el valor 2
# corresponda a papel y el valor 3 corresponda a tijera

# from random import  randint
#
# ana = random.randint(1, 3)
# juan = random.randint(1, 3)
#
# print(f"Ana elige: {'piedra' if ana == 1 else 'papel' if ana == 2 else 'tijera'}")
# print(f"Juan elige: {'piedra' if juan == 1 else 'papel' if juan == 2 else 'tijera'}")
#
#
# if ana == juan:
#     print("Empate")
# elif (ana == 1 and juan == 3) or (ana == 2 and juan == 1) or (ana == 3 and juan == 2):
#     print("Ana gana")
# else:
#     print("Juan gana")


# EJERCICIO 11
# Escribir un programa que pida el numero de golpes que ha
# necesitado un jugador de golf para hacer hoyo y el par del
# hoyo que es numero ideal de golpes El programa debe calcular
# la puntuación del jugador que depende de los valores anterior
# mediante el siguiente resumen. El programa deberá mostrar el
# mensaje correspondiente según la puntuación que obtenga el jugador



numGolpes = int(input("Ingrese el número de golpes del jugador: "))

if numGolpes == 0:
    print(" Golfista aun no empezó")
else:
    parHoyo = int(input("Ingrese el par del hoyo: "))
    puntuacion = numGolpes - parHoyo
    if puntuacion == 0:
        print("Hole-in-one!")
    elif puntuacion <= -2:
        print("Eagle")
    elif puntuacion == -1:
        print("Birdie")
    elif puntuacion == 0:
        print("Par")
    elif puntuacion == 1:
        print("Bogey")
    elif puntuacion == 2:
        print("Double Bogey")
    else:
        print("Go Home!")