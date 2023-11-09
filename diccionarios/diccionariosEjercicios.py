# Ejercicio 24
# Crear un programa que dado un numero entero nos muestre cada
# uno de sus dígitos escritos con palabras. Comprobar que la
# entrada es numérica

diccionario={
    0:"cero",
    1:"uno",
    2:"dos",
    3:"tres",
    4:"cuatro",
    5:"cinco",
    6:"seis",
    7:"siete",
    8:"ocho",
    9:"nueve"
}

resultado=""
numero=input("Escribe un numero: ")

if numero.isnumeric():
    for num in numero:
        resultado += diccionario[int(num)]+" "

print(resultado)

#Ejercicio 25
# Crear un programa que dado un texto con emojis expresados como
# stirng imprima el mismo texto pero con los emojis en forma
# directa, por ejemplo I am sad I am sad ☹ El programa
# debe al menos admitir 10 emojis distintos

emojis = {
    ":)": "😊",
    ":(": "☹",
    ":D": "😄",
    ":O": "😲",
    ":P": "😛",
    ";)": "😉",
    "<3": "❤️",
    ":|": "😐",
    ":*": "😘",
    ":/": "😕"
}

texto = ":( :) :/ u:"
for iconos in emojis:
    texto = texto.replace(iconos, emojis[iconos])

print(texto)

# EJERCICIO 26
# Crear un programa que reciba una serie de nombres separados
# por comas y después una serie de números que representan
# edades El programa debe generar un diccionario donde la clave
# son los los nombres y los valores las edades Primero
# intentarlo usando bucles y después otra versión usando la función zip

nombres=["Jose","Kike","Ruben","David","Fabio"]
edades=[37,32,30,19,20]

diccionario=dict(zip(nombres,edades))

print(diccionario)

for i in range(len(nombres)):
    diccionario[nombres[i]] = edades[i]

print(diccionario)