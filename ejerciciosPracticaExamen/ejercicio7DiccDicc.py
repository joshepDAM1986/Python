# EJERCICIO 7
# Escribir un programa que permita gestionar la base de datos de una tienda de videojuegos. Los
# datos se deben transformar a una lista de diccionarios a partir del siguiente string:
# Juego;Precio;Genero;Disponible
# Super Mario Bros;30.0;Plataformas;True
# Silent Hill;12.0;Terror;False
# Resident Evil;45.0;Terror;False
# Halo 5;20.0;Shooter;True
# Final Fantasy VII;19.90;JRPG;True
# PES 2021;9.99;Deportivo;True
# FIFA 2022;59.99;Deportivo;False
# Posteriormente hacer un menú de opciones que permita hacer lo siguiente:
# 1) Buscar un juego por nombre.
# 2) Listar todos los juegos que esten disponibles.
# 3) Mostrar los juegos (solo nombre y precio) ordenados según el precio de manera descendente.
# 4) Mostrar los juegos (solo su nombre) en orden alfabetico normal.
# 5) Mostrar nombre y el precio del juego más barato.
# 6) Crear un string a partir de la lista con el mismo formato del que se ha utilizado de entrada.
# 7) Crear un diccionario con los juegos cuyo precio sea menor de X y esten disponibles. La clave
# debe ser el nombre y el valor el precio.

transformar = {
    "int": int,
    "float": float,
    "boolean": eval,
}

def es_float(cadena):
    partes = cadena.split(".")
    return (len(partes) == 2 and
     partes[0].isdigit() and
     partes[1].isdigit())

def tipo(cadena):
    if cadena.isdigit():
        return "int"
    elif es_float(cadena):
        return "float"
    elif cadena.lower() == "true" or cadena.lower() == "false":
        return "boolean"
    else:
        return "string"

def castear_datos(diccionario):
    for (clave, valor) in diccionario.items():
        tipo_valor = tipo(valor)
        diccionario[clave] = transformar.get(tipo_valor, lambda x: x)(valor)

juegos = """Juego;Precio;Genero;Disponible
Super Mario Bros;30.0;Plataformas;True
Silent Hill;12.0;Terror;False
Resident Evil;45.0;Terror;False
Halo 5;20.0;Shooter;True
Final Fantasy VII;19.90;JRPG;True
PES 2021;9.99;Deportivo;True
FIFA 2022;59.99;Deportivo;False"""

lineas = juegos.split("\n")
cabecera = lineas[0].split(";")

diccJuegos={}

for linea in lineas[1:]:
    juego=dict(zip(cabecera, linea.split(";")))
    castear_datos(juego)
    diccJuegos[juego["Juego"]]=juego
print(diccJuegos)

def buscarJuegoNombre(nombre, diccJuegos):
    return diccJuegos.get(nombre)

def listarJuegosDisponibles(diccJuegos):
    for clave, valor in diccJuegos.items():
        if valor["Disponible"]:
            print(diccJuegos[clave])
def mostrarNombrePrecioDesc(diccJuegos):
    juegosOrdenados = sorted(diccJuegos.items(), key=lambda x: x[1]["Precio"], reverse=True)
    for nombre, juegoInfo in juegosOrdenados:
        print(f"{nombre}: {juegoInfo['Precio']}")

def mostrarJuegosAlfabetico(diccJuegos):
    juegosAlfabetico = sorted(diccJuegos.items())
    for nombre in juegosAlfabetico:
        print(nombre)

def mostrarJuegoBarato(diccJuegos):
    juegoBarato = min(diccJuegos.items(), key=lambda x: x[1]["Precio"])
    print(juegoBarato)

def crearString(diccJuegos):
    nuevoString = ";".join(cabecera)
    for nombre, juegoInfo in diccJuegos.items():
        juego_info_str = [str(juegoInfo[cabecera]) for cabecera in cabecera]
        nuevoString += "\n" + ";".join(juego_info_str)
    print(nuevoString)

def crearDiccionario(minPrecio, diccJuegos):
    nuevoDiccionario = {
        nombre: juegoInfo["Precio"]
        for nombre, juegoInfo in diccJuegos.items()
        if juegoInfo["Disponible"] and juegoInfo["Precio"] < minPrecio
    }
    return nuevoDiccionario

bucle=True
while bucle:

    print("\n------------------------------MENU------------------------------------")
    print("1). Buscar juego por nombre")
    print("2). Listar juegos disponibles")
    print("3). Listar juegos ordenados por precio descendente")
    print("4). Lista juegos ordenados Alfabeticamente")
    print("5). Mostrar nombre y el precio del juego más barato.")
    print("6). Crear un string a partir del diccionario con el mismo formato")
    print("7). Crear un diccionario con los juegos cuyo precio sea menor de X")
    print("0). Salir")

    opcion = input("Introduzca una opción: ")

    if opcion == "1":
        nombreJuego = input("Introduce el nombre del juego: ")
        juegoEncontrado = buscarJuegoNombre(nombreJuego, diccJuegos)
        if juegoEncontrado:
            print(juegoEncontrado)
        else:
            print("No existe el juego")

    elif opcion == "2":
        listarJuegosDisponibles(diccJuegos)

    elif opcion == "3":
        mostrarNombrePrecioDesc(diccJuegos)

    elif opcion == "4":
        mostrarJuegosAlfabetico(diccJuegos)

    elif opcion == "5":
        mostrarJuegoBarato(diccJuegos)

    elif opcion == "6":
        crearString(diccJuegos)

    elif opcion == "7":
        minPrecio = float(input("¿Cuál es el precio límite? "))
        nuevoDiccionario = crearDiccionario(minPrecio, diccJuegos)
        print(nuevoDiccionario)

    elif opcion == "0":
        bucle=False

    else:
        print("Opción no válida")