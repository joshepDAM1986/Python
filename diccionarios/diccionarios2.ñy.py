# lista_frutas=[{
#            "nombre":"manzana",
#            "precio":2.4,
#            "categoria":"A"
#        },
#        {
#            "nombre":"peras",
#            "precio":1.3,
#            "categoria":"B"
#        },
#        {
#            "nombre":"naranjas",
#            "precio":4.4,
#            "categoria":"C"
#        }]


# buscado=input("Dime un nombre de fruta: ")
# info=None
#
# for fruta in lista_frutas:
#     if fruta["nombre"]==buscado:
#         print(fruta)
#         break # termina el bucle
#     if info==None:
#         info=fruta
#         print("No existe esa fruta")
#     else:
#         print(info)



# for fruta in lista_frutas:
#     if fruta ["precio"]>2 and fruta["categoria"]=="C":
#         print(fruta["nombre"])


dicc_frutas={
        "Manzana":{
            "nombre":"manzana",
            "precio":2.4,
            "categoria":"A"},
        "Peras":{
           "nombre":"peras",
           "precio":1.3,
           "categoria":"B"},
        "Naranjas":{
           "nombre":"naranjas",
           "precio":4.4,
           "categoria":"C"}
        }

print(dicc_frutas["Peras"]["precio"]) #imprime el precio de las peras

buscado=input("Dime el nombre de una fruta: ")
info=dicc_frutas.get(buscado.lower(),"No existe")
print(info)

for fruta in dicc_frutas.values():
    print(fruta)

#datos en bruto
datos="""nif;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lista_clientes=[]
lineas=datos.split("\n")
cabezera=lineas[0].split(";")#lista con claves del diccionario

for linea in lineas[1:]:# así nos saltamos la primera linea de datos porque hay 4 clientes y 5 lineas.
    partes=linea.split(";")
    cliente=dict(zip(cabezera,cliente))
    cliente["descuento"]=float(cliente["descuento"])
    # for i in range(len(cabezera)):
    #     partes = linea.split(";")
    #     cliente[cabezera[i]]=partes[i]
    # cliente["nif"]=partes[0]
    # cliente["nombre"] = partes[1]
    # cliente["email"] = partes[2]
    # cliente["telefono"] = partes[3]
    # cliente["descuento"] = partes[4]
    lista_clientes.append(cliente)
print(lista_clientes)