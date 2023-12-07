datos_peliculas = """titulo,genero,minutos,recaudacion,disponible
Los Vengadores,superheroes,140,367.86,True
La Monja,terror,100,123.57,False
El Reino,suspense,90,21.54,False
Scream 3,terror,123,300.12,True
Pulp fiction,drama,150,98.3,False
La liga de la Justicia,superheroes,120,190.12,True"""

tipo_datos = {
    "int": int,
    "float": float,
    "boolean": eval
}


def es_float(valor):
    partes = valor.split(".")
    return len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit()


def tipo(valor):
    if valor.isdigit():
        return "int"
    elif es_float(valor):
        return "float"
    elif valor.lower() == "true" or valor.lower() == "false":
        return "boolean"
    else:
        return "string"


def castear_datos(diccionario):
    for clave, valor in diccionario.items():
        tipo_dato = tipo(valor)
        diccionario[clave] = tipo_datos.get(tipo_dato, lambda x: x)(valor)

# INICIO DEL PROGRAMA

lineas = datos_peliculas.split("\n")
cabecera = lineas[0].split(",")
diccionarioPeliculas = {}

for linea in lineas[1:]:
    pelicula = dict(zip(cabecera, linea.split(",")))
    castear_datos(pelicula)
    diccionarioPeliculas[pelicula["titulo"]]=pelicula

opcion = -1
while opcion != 0:
    opcion = int(input("""0.Salir
1.Ordenar
2.Menos rentable
3.Filtro
4.Exportar
"""))
    if opcion == 0:
        print("Adios")
    elif opcion == 1:
        ordenados = sorted(diccionarioPeliculas.values(), key=lambda x: x["minutos"], reverse=True)
        res = ""
        for pelicula in ordenados:
            if pelicula["disponible"]:
                res += str(pelicula) + "\n"
        print(res)
    elif opcion == 2:
        menos = min(diccionarioPeliculas.values(), key=lambda x: x["recaudacion"])
        print(f"{menos['titulo']}")
    elif opcion == 3:
        nuevoDic = {}
        for pelicula in diccionarioPeliculas.values():
            if pelicula["minutos"] < 120:
                nuevoDic[pelicula["titulo"]] = pelicula["minutos"]
        print(nuevoDic)
    elif opcion == 4:
        cabecera=list(diccionarioPeliculas.values())[0].keys()
        res=",".join(cabecera)+"\n"

        for pelicula in diccionarioPeliculas.values():
            for clave,valor in pelicula.items():
                pelicula[clave]=str(valor)
            res+= ",".join(pelicula.values()) + "\n"
        print(res)

