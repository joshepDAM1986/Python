# DISFRAZ_DEFECTO = "PECERA"

# adversario = input("Quien tienes enfrente ")
# if adversario.lower() == "loki":
#     misterio = "Lady Loki"
# elif adversario.lower() == "hulk":
#     misterio = "Thanos"
# elif adversario.lower() == "thor":
#     misterio = "Odin"
# elif adversario.lower() == "superman":
#     misterio = "Darkseid"
# else:
#     misterio = DISFRAZ_DEFECTO

# disfraces_misterio={
#        "superman":"Darkseid",
#        "thor":"Odin",
#        "loki":"Lady Loki",
#        "hulk":"Thanos"
#     }
# print(disfraces_misterio.get(adversario.lower(), DISFRAZ_DEFECTO))

from random import choice

def funcionSumar(lista):
    res = 0
    for num in lista:
        res += num
    return res

def funcionMultiplicar(lista):
    res = 1
    for num in lista:
        res *= num
    return res

def funcionRandom(lista):
    return choice(lista)

def funcionOrdenar(lista):
    return sorted(lista)

funciones = {
    "sum": funcionSumar,
    "multi": funcionMultiplicar,
    "ale": funcionRandom,
    "ord": funcionOrdenar
}

numeros = [5, 2, 4, 3, 1]
operacion = input("Que operacion quieres realizar? ")

if operacion == "sum":
    res = 0
    for num in numeros:
        res += num
elif operacion == "multi":
    res = 1
    for num in numeros:
        res *= num
elif operacion == "ale":
    res = choice(numeros)
else:
    res = "No existe"

selecciom = funciones.get(operacion.lower(), lambda x: "No existe")
print(selecciom(numeros))
