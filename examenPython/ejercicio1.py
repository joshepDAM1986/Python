opcion=input("Dime una operacion a realizar: ")
numero=input("Dime un numero: ")

def funFactorial(numero):
    numero = int(numero)
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i

    return f"El factorial de {numero} es {resultado}"

def funPotencia(numero):
    numero = float(numero)
    exponente = int(input("Dime el exponente: "))
    resultado = 1

    for _ in range(exponente):
        resultado *= numero

    return f"{numero} elevado a la potencia {exponente} es {resultado}"

funciones = {
    "factorial":funFactorial,
    "potencia":funPotencia
}

seleccion= funciones.get(opcion.lower(), lambda x:"No existe esta operacion")
print(seleccion(numero))