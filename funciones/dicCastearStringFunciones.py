def es_float(cadena):
    partes = cadena.split(".")
    return (len(partes) == 2
            and partes[0].isdigit()
            and partes[1].isdigit())

def tipo(cadena):
    if cadena.isdigit():
        return "int"
    elif es_float(cadena):
        return "float"
    elif cadena.lower()=="true" or cadena.lower()=="false":
        return "boolean"
    else:
        return "string"

def castear_datos(persona):
    for (atributo, valor) in persona.items():
        tipo_valor = tipo(valor)
        if tipo_valor == "int":
            persona[atributo] = int(valor)
        elif tipo_valor == "float":
            persona[atributo] = float(valor)
        elif tipo_valor == "boolean":
            persona[atributo] = eval(valor)

datos = """dni;nombre;email;teléfono;descuento;vip
01234567L;Luis González;luisgonzalez@mail.com;+34656343576;12.5;True
71476342J;Macarena Ramírez;macarena@mail.com;+34692839321;8.0;False
63823376M;Juan José Martínez;juanjo@mail.com;+34664888233;5.2;True
98376547F;Carmen Sánchez;carmen@mail.com;+34667677855;15.7;False"""

lineas = datos.split("\n")
cabecera = lineas[0].split(";")

lista_clientes = []
for linea in lineas[1:]:
    persona = dict(zip(cabecera, linea.split(";")))
    castear_datos(persona)
    lista_clientes.append(persona)
print(lista_clientes)

# Diccionario de diccionarios
dicc_clientes = {}
for linea in lineas[1:]:
    persona = dict(zip(cabecera, linea.split(";")))
    castear_datos(persona)
    dicc_clientes[persona["dni"]] = persona;
print(dicc_clientes)