# EJERCICIO 1
# Sin usar condicionales y usando diccionarios con funciones def hacer un programa que sea equivalente a lo  siguiente en un fichero llamado ejercicio1.py:
# IMPORTANTE¡¡Factorial y potencia programarlo con bucles, no vale usar la libreria Math ó **

def factorial(numero):
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


def potencia(numero):
    resultado = 1
    for i in range(numero):
        resultado *= 2
    return resultado


funciones = {
    "factorial": factorial,
    "potencia": potencia
}

numero = int(input("Dime un numero:"))
operacion = input("Dime una operacion a realizar:")
seleccion = funciones.get(operacion, lambda x: "No existe esa operacion")(numero)
print(seleccion)
