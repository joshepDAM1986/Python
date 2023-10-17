#string.py

lenguaje="python"
#
# #Posición
# print(lenguaje[0])
# print(lenguaje[1])
# print(lenguaje[5])
# print(lenguaje[-1])
# print(lenguaje[-2])
#
# ultimo=len(lenguaje)-1
# print(lenguaje[ultimo])
# print(lenguaje[len(lenguaje)-1])
#
# #Rangos
# print(lenguaje[1:3]) #Rango de caracteres inclusivo:exclusivo
#
# print(lenguaje[1:4])
# print(lenguaje[1:1])
# print(lenguaje[1:])
# print(lenguaje[1:5:2])
#
#
# #Repetición
# print(lenguaje*3)
#
# #Exixtencia
# print("y" in lenguaje)
# print("a" not in lenguaje)
# print("thon" in lenguaje)

#Comparaciones
print(lenguaje=="python")
print(lenguaje=="Python")
print(lenguaje!="python")
print("abc">lenguaje)
print("abc"<lenguaje)

print("123"<"45") #Compara si 1 es mayor que 4.

#Transformaciones (las variables son inmutable)
print(lenguaje.upper())
print(lenguaje.lower())
print(lenguaje.capitalize())
print(lenguaje)

#Comparaciones .is
print(lenguaje.isnumeric()) #Compara si solo numerico
print(lenguaje.isalpha()) #Compara si solo son caracteres
print(lenguaje.isalnum()) #Compara si no hay caracteres especiales

