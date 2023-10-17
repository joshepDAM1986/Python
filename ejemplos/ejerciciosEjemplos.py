# EJERCICIO 1
# Escribir un programa que pida al usuario su peso (en kg) y
# estatura (en metros), calcule el índice de masa corporal
# redondeado a 2 decimales.

# peso = float(input("Ingrese su peso en kg: "))
# estatura = float(input("Ingrese su estatura en metros: "))
# imc = (round(peso / (estatura ** 2),2))
# print("Su índice de masa corporal (IMC) es: ", imc)

# EJERCICIO 2
# Escribir un programa que pida una cantidad de días y las
# convierta a horas minutos y segundos. Usar templates para
# mostrar los datos.

# dias = int(input("Ingrese la cantidad de días: "))
#
# horas = dias * 24
# minutos = horas * 60
# segundos = minutos * 60
#
# print("{} días son equivalentes a:".format(dias))
# print("Horas: {}".format(horas))
# print("Minutos: {}".format(minutos))
# print("Segundos: {}".format(segundos))

# EJERCICIO 3
# Escriba un programa conversor de centímetros a kens y shakus,
# unidades japonesas de longitud. Un ken son seis shakus y un
# shaku equivale a 30,3 cm. Se pedirá una cantidad de
# centímetros y mostrar los resultados con 2 decimales.

# centimetros = float(input("Ingrese la cantidad de centímetros: "))
#
# shakus = centimetros / 30.3
# kens = shakus / 6
#
# print("{:.2f} centímetros son equivalentes a:".format(centimetros))
# print("{:.2f} shakus".format(shakus))
# print("{:.2f} kens".format(kens))

# EJERCICIO 4
# Investigar como escribir un programa que transforme un número
# expresado en binario como un string, a base decimal sin bucles
# usando la función int.


binario = input("Ingrese un número binario: ")

decimal = int(binario, 2)

print("El número decimal equivalente es:", decimal)