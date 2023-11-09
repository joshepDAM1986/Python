import random

# EJERCICIO 12
# Escribe un programa que pida datos al usuario hasta que
# escriba una cadena alfanumérica

# while True:
#     entrada = input("Ingrese un dato: ")
#     if entrada.isalnum():
#         print("¡Perfecto! Has ingresado una cadena alfanumérica.")
#         break
#     else:
#         print("Por favor, ingresa una cadena alfanumérica.")


# EJERCICIO 13
# Escribe un programa que pida un numero por pantalla y usando
# un solo while escriba un triangulo y un cuadrado de asteriscos

# numero = int(input("Ingrese un número: "))
#
# #triángulo
# print("\nTriángulo:")
# iT = 1
# while iT <= numero:
#     print('*' * iT)
#     iT += 1
#
# #cuadrado
# print("\nCuadrado:")
# iC = 1
# while iC <= numero:
#     print('*' * numero)
#     iC += 1


# EJERCICIO 14
# Escribe un programa que genere un número aleatorio entre 1 y
# 50 Después el usuario intentará acertarlo

# numSecreto = random.randint(1, 50)
#
# print("¡Bienvenido al juego de adivinanzas!")
# intentos = 0
#
# while True:
#     intento = int(input("Intenta adivinar el número (entre 1 y 50): "))
#
#     intentos += 1
#
#     if intento == numSecreto:
#         print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
#         break
#     elif intento < numSecreto:
#         print("El número es mayor. ¡Sigue intentando!")
#     else:
#         print("El número es menor. ¡Sigue intentando!")


# EJERCICIO 15
# Escribe un programa similar al anterior, pero donde el propio
# programa sea el que intenta acertar un número que piensa el
# usuario generando aleatorios El usuario responde s o n hasta
# que el programa acierta el número Hacerlo de manera lo más
# inteligente posible y no solo con números al azar en el rango
# 1:50

print("Piensa en un número entre 1 y 50, yo intentaré adivinarlo.")

limiteInferior = 1
limiteSuperior = 50
intentos = 0

while (intentos < 5):
    numPensado = random.randint(limiteInferior, limiteSuperior)
    intentos += 1
    respuesta = input(f"¿Es {numPensado} tu número? (s/n): ").lower()

    if intentos==5:
        print("No he conseguido averiguar el número")
        break

    if respuesta == 's':
        print(f"¡Adiviné tu número en {intentos} intentos! Es {numPensado}.")
        break
    elif respuesta == 'n':
        ajuste = input("¿Es el número mayor (+) o menor (-) que tu número? ")
        if ajuste == '+':
            limiteInferior = numPensado + 1
        elif ajuste == '-':
            limiteSuperior = numPensado - 1
        else:
            print("Por favor, ingresa '+' o '-'.")
    else:
        print("Por favor, ingresa 's' o 'n'.")