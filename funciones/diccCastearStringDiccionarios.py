def es_float(cadena):
    partes = cadena.split(".")
    (len(partes) == 2 and
     partes[0].isdigit() and
     partes[1].isdigit())

def tipo(cadena):
    if cadena.isdigit():
        return "int"
    elif es_float(cadena):
        return "float"
    elif cadena.lower()=="true" or cadena.lower()=="false":
        return "boolean"
    else:
        return "string"

transformer={
    "int":int,
    "float":float,
    "boolean":eval,
}

def castear_datos(persona):
    for (atributo,valor) in persona.items():
        tipo_valor=tipo(valor)
        funcionTipo = transformer.get(tipo_valor.lower(), lambda x:x)
        
        persona[atributo]=funcionTipo(valor)
        # Lo mismo pero en una sola linea
        persona[atributo]=transformer.get(tipo_valor,lambda x:x)(valor)

datos="""dni;nombre;email;teléfono;descuento;vip;edad
01234567L;Luis González;luisgonzalez@mail.com;+34656343576;12.5;True;34
71476342J;Macarena Ramírez;macarena@mail.com;+34692839321;8.0;False;27
63823376M;Juan José Martínez;juanjo@mail.com;+34664888233;5.2;True;42
98376547F;Carmen Sánchez;carmen@mail.com;+34667677855;15.7;False;85"""

lineas=datos.split("\n")

cabecera=lineas[0].split(";")
lista_clientes=[]
for linea in lineas[1:]:
    persona=dict(zip(cabecera,linea.split(";")))
    castear_datos(persona)
    lista_clientes.append(persona)
print(lista_clientes)

# Diccionario de diccionarios
dicc_clientes={}
for linea in lineas[1:]:
    persona=dict(zip(cabecera,linea.split(";")))
    castear_datos(persona)
    dicc_clientes[persona["dni"]]=persona;
print(dicc_clientes)