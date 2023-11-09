# import math
# print(math.pi)
# print(math.gcd(16,12))
#-----------------------
# from math import pi
# from math import gcd
# from math import factorial
# from random import  random
# from random import  randint

# from datetime import datetime

# print(pi)
# print(gcd(16,12))
# print(factorial(5))
# print((random()))
# print(randint(0,10))

# print(datetime.now().date())
# print(datetime.now().time())

# Condicionales

# numero=int(input("Escribe un numero positivo"))
# if numero<0:
#     print("Es negativo")
# elif 0>=0 and numero < 18:
#     print("Si fuera una edad serias menor de edad")
# else:
#     print("No es negativo ni menor de 18")
#
# numero=int(input("Escribe un numero positivo"))
# if numero < 0:
#     print("Te he dicho que sea positivo ostias")
#     print(f"Has escrito el numero {numero}")
# else:
#     print("Nooooooo")

# edad=int(input("Digame su edad "))
# if edad<120:
#     pass
# else:
#     print("No me lo creo")
numero=int(input("Escriba un numero: "))
if numero%2:
    print(f"{numero} es impar")
else:
    print(f"{numero} es par")
