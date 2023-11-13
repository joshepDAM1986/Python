#
# def por_definir():
#     pass
#
# def sumar(a,b):
#     return a+b
#
# def sumar_lista(numeros):
#     total=0
#     for i in numeros:
#         total+=i
#     return total
#
# resultado=sumar(1,5)
# print(resultado)
# print(sumar_lista([1,2,3,4,5]))
#
# def potencia(base, exponente=2): #2 es el valor por defecto del exponente
#     return base**exponente
#
# print(potencia(4)) # usa el valor por defecto del exponente
# print(potencia(4,3)) # sustituye el valor por defecto de exponente por ingresado
# print(potencia(exponente=3, base=2))
#
# def funcion(dato):
#     dato+=2
#     print(dato)
#
#
#
# def funcion_lista(lista):
#     lista[0]=5
#     print(lista)
#
# numeros=[10,20,30,40]
# funcion_lista(numeros)
# print(numeros)
#
# # numero=33
# # funcion(numero)
# # print(numero)
#
# def funcion_diccionario(dic):
#     dic["nombre"]="Pedro"
#     print(dic)
#
# persona={
#     "nombre":"Juan",
#     "edad":25
# }
# print(persona)
#
# funcion_diccionario(persona)
# print(persona)

lista_frutas=[{
           "nombre":"Manzana",
           "precio":2.4,
           "categoria":"A"
       },
       {
           "nombre":"Peras",
           "precio":1.3,
           "categoria":"B"
       },
       {
           "nombre":"Naranjas",
           "precio":4.4,
           "categoria":"C"
       }]


def criterio(fruta):
    return fruta["nombre"]

print(max(lista_frutas, key=criterio))
ordenada=(sorted(lista_frutas,key=criterio))

for fr in ordenada:
    print(fr["nombre"])


frutaMasbarata=min(lista_frutas, key=lambda  f:f["nombre"])
print(frutaMasbarata["nombre"])

frutasOrdenadas=sorted(lista_frutas,key=lambda  fruta:fruta["nombre"])