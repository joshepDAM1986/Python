# # Ejercicio 24
# # Crear un programa que dado un numero entero nos muestre cada
# # uno de sus dígitos escritos con palabras. Comprobar que la
# # entrada es numérica
#
# diccionario={
#     0:"cero",
#     1:"uno",
#     2:"dos",
#     3:"tres",
#     4:"cuatro",
#     5:"cinco",
#     6:"seis",
#     7:"siete",
#     8:"ocho",
#     9:"nueve"
# }
#
# resultado=""
# numero=input("Escribe un numero: ")
#
# if numero.isnumeric():
#     for num in numero:
#         resultado += diccionario[int(num)]+" "
#
# print(resultado)
#
# #Ejercicio 25
# # Crear un programa que dado un texto con emojis expresados como
# # stirng imprima el mismo texto pero con los emojis en forma
# # directa, por ejemplo I am sad I am sad ☹ El programa
# # debe al menos admitir 10 emojis distintos
#
# emojis = {
#     ":)": "😊",
#     ":(": "☹",
#     ":D": "😄",
#     ":O": "😲",
#     ":P": "😛",
#     ";)": "😉",
#     "<3": "❤️",
#     ":|": "😐",
#     ":*": "😘",
#     ":/": "😕"
# }
#
# texto = ":( :) :/ u:"
# for iconos in emojis:
#     texto = texto.replace(iconos, emojis[iconos])
#
# print(texto)
#
# # EJERCICIO 26
# # Crear un programa que reciba una serie de nombres separados
# # por comas y después una serie de números que representan
# # edades El programa debe generar un diccionario donde la clave
# # son los los nombres y los valores las edades Primero
# # intentarlo usando bucles y después otra versión usando la función zip
#
# nombres=["Jose","Kike","Ruben","David","Fabio"]
# edades=[37,32,30,19,20]
#
# diccionario=dict(zip(nombres,edades))
#
# print(diccionario)
#
# for i in range(len(nombres)):
#     diccionario[nombres[i]] = edades[i]
#
# print(diccionario)
#
# # EJERCICIO27
# # Crear un programa que partiendo del siguiente texto
# # """
# # nif;nombre;email;teléfono;descuento n01234567L;Luis
# # González;luisgonzalez@mail.com;656343576;12.5 n71476342J;Macarena
# # Ramírez;macarena@mail.com;692839321;8 n63823376M;Juan José
# # Martínez;juanjo@mail.com;664888233;5.2 n98376547F;Carmen
# # Sánchez;carmen@mail.com;667677855;15.7
#
# texto = ("nif;nombre;email;teléfono;descuento\n"
#          "01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n"
#          "71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n"
#          "63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n"
#          "98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7")
#
# lineas = texto.split('\n')
# encabezado = lineas[0].split(';')
#
# listTexto = []
# for linea in lineas[1:]:
#     campos = linea.split(';')
#     diccionario = dict(zip(encabezado, campos))
#     listTexto.append(diccionario)
# print(listTexto)
#
# dicTexto = {}
# for linea in lineas[1:]:
#     campos = linea.split(";")
#     dicTexto[campos[0]] = dict(zip(encabezado[1:], campos[1:]))
# print(dicTexto)

# EJERCICIO 27_PROF

datos="""dni;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;+34656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;+34692839321;8.0
63823376M;Juan José Martínez;juanjo@mail.com;+34664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;+34667677855;15.7"""


lineas=datos.split("\n")

cabecera=lineas[0].split(";")
lista_clientes=[]

for linea in lineas[1:]:
    persona=dict(zip(cabecera,linea.split(";")))
    persona["descuento"]=float(persona["descuento"])
    lista_clientes.append(persona)
print(lista_clientes)

#Diccionario de diccionarios

# dicc_clientes={}
# for linea in lineas[1:]:
#     persona=dict(zip(cabecera,linea.split(";")))
#     persona["descuento"]=float(persona["descuento"])
#     dicc_clientes[persona["dni"]]=persona;
# print(dicc_clientes)
