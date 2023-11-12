# EJERCICIO 3:
# Realizar un programa que genere contraseñas aleatorias. El programa pide cuantas contraseñas se van generar y
# después la longitud de las mismas. Los caracteres admitidos en las contraseñas son:
# 0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz

import random

numContraseñas=int(input("Ingrese el numero de contraeñas: "))
longContraseñas=int(input("Ingrese cuan larga será la contraseña: "))
cadena="0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz"

for i in range(numContraseñas):
    contContraseña = i + 1
    resultado = ""
    for i in range(longContraseñas):
        resultado += random.choice(cadena)
    print(f"Contraseña {contContraseña}: {resultado}")