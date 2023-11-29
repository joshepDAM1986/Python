# EJERCICIO 3:
# Realizar un programa que genere contraseñas aleatorias. El programa pide cuantas contraseñas se van generar y
# después la longitud de las mismas. Los caracteres admitidos en las contraseñas son:
# 0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz

import random

numContraseñas=int(input("Ingrese el numero de contraseñas: "))
longContraseñas=int(input("Ingrese la longitud de las contraseñas: "))
cadena="0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz"

for i in range(numContraseñas):
    contContraseña = i + 1
    resultadoCadena = ""
    for i in range(longContraseñas):
        resultadoCadena += random.choice(cadena)
    print(f"Contraseña {contContraseña}: {resultadoCadena}")

print("-----------------------------------------------------------------------------------------------------------------")

listaCadena=list(cadena)
print(listaCadena)

for i in range(numContraseñas):
    contContraseña = i + 1
    resultadoLista=""
    for i in range(longContraseñas):
        resultadoLista+=random.choice(listaCadena)
    print(f"Contraseña {contContraseña}: {resultadoLista}")

