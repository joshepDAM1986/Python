
# EJERCICIO 4:
# A partir del fichero ejercicio4.py que contiene un string con la siguiente informacion organizada por lineas y separadores:

datos_peliculas = """titulo,genero,minutos,recaudacion,disponible
Los Vengadores,superheroes,140,367.86,True
La Monja,terror,100,123.57,False
El Reino,suspense,90,21.54,False
Scream 3,terror,123,300.12,True
Pulp fiction,drama,150,98.3,False
La liga de la Justicia,superheroes,120,190.12,True"""

# Realizar las siguiente acciones:
# a)	(2 Puntos). A partir del string anterior crear una lista de diccionarios que permita reflejar de manera estructurada la información. Se debe programar de manera que el código sea lo más independiente posible de la información de entrada como se vio en clase.
# b)	(0,5 Puntos). Mostrar un menú de opciones como el siguiente que realizan operaciones sobre la estructura de datos anterior:
# 0. Salir.
# 1. Ordenar.
# 2. Menos rentable.
# 3. Filtro.
# 4. Exportar.
# El menú se repetirá mediante un bucle while y solo se saldrá si el usuario elije la opción 0.
# c)	(3 Puntos). Implementar cada opcion del menú de la manera indicada.
# •	Opción 1 (0,75 puntos). Mostrar ordenada la lista de peliculas disponibles ordendas por minutos de duración de mayor a menor
# •	Opción 2 (0,5 puntos). Mostrar el nombre de la pelicula que ha recaudado menos dinero.
# •	Opción 3 (0,75 puntos). Crear una diccionario con solo las peliculas que duren menos de 120 minutos, donde la clave del diccionario es el nombre de la pelicula y el valor los minutos. Mostrar el diccionario al final del proceso con haciendo un print del mismo.
# •	Opción 4 (1 punto). Convertir la lista de diccionarios en un string similar al de origen y mostrarlo por pantalla.



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
listaPeliculas = []

for linea in lineas[1:]:
    pelicula = dict(zip(cabecera, linea.split(",")))
    castear_datos(pelicula)
    listaPeliculas.append(pelicula)

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
        ordenados = sorted(listaPeliculas, key=lambda x: x["minutos"], reverse=True)
        res = ""
        for pelicula in ordenados:
            if pelicula["disponible"]:
                res += str(pelicula) + "\n"
        print(res)
    elif opcion == 2:
        menos = min(listaPeliculas, key=lambda x: x["recaudacion"])
        print(f"{menos['titulo']}")
    elif opcion == 3:
        nuevoDic = {}
        for pelicula in listaPeliculas:
            if pelicula["minutos"] < 120:
                nuevoDic[pelicula["titulo"]] = pelicula["minutos"]
        print(nuevoDic)
    elif opcion == 4:
        res=",".join(listaPeliculas[0].keys())+"\n"
        for pelicula in listaPeliculas:
            for clave,valor in pelicula.items():
                pelicula[clave]=str(valor)
            res+= ",".join(pelicula.values()) + "\n"
        print(res)

