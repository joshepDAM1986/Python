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

# listaJuegos = []
#
# for linea in lineas[1:]:
#     juego = dict(zip(cabecera, linea.split(";")))
#     juego["Precio"] = float(juego["Precio"])
#     juego["Disponible"] = eval(juego["Disponible"])
#     listaJuegos.append(juego)
# print(listaJuegos)

diccJuegos={}

for linea in lineas[1:]:
    juego=dict(zip(cabecera, linea.split(";")))
    juego["Precio"]=float(juego["Precio"])
    juego["Disponible"]=eval(juego["Disponible"])
    diccJuegos[juego["Juego"]]=juego;
print(diccJuegos)

# PARA LISTA-DICCIONARIO
# def buscarJuegoNombre(nombre, listaJuegos):
#     for juego in listaJuegos:
#         if juego["Juego"] == nombre:
#             return juego
#     return None
#
# def listarJuegosDisponibles(listaJuegos):
#     listaJuegosDisponibles=[]
#     for juego in listaJuegos:
#         if juego["Disponible"]:
#             listaJuegosDisponibles.append(juego)
#     return listaJuegosDisponibles
#
# def mostrarNombrePrecioDesc(listaJuegos):
#     listaJuegosOrdenados=sorted(listaJuegos, key= lambda x: x["Precio"], reverse=True)
#     for juego in listaJuegosOrdenados:
#         print(f"{juego['Juego']}:{juego['Precio']}")
#
# def mostrarJuegosAlfabetico(listaJuegos):
#     listaJuegosAlfabetico=sorted(listaJuegos, key=lambda x: x["Juego"])
#     for juego in listaJuegosAlfabetico:
#         print(f"{juego['Juego']}")
#
# def mostrarJuegoBarato(listaJuegos):
#     juegoBarato= min(listaJuegos, key=lambda x: x ["Precio"])
#     print(juegoBarato)
#
# def crearDiccionario(minPrecio, listaJuegos):
#     nuevoDiccionario={}
#     for juego in listaJuegos:
#         if juego["Disponible"] and juego["Precio"]<minPrecio:
#             nuevoDiccionario[juego['Juego']]=juego['Precio']
#     return nuevoDiccionario

# PARA DICCIONARIO-DICCIONARIO
def buscarJuegoNombre(nombre, diccJuegos):
    if nombre in diccJuegos:
        juego = diccJuegos[nombre]
        print(f"Datos de {nombre}:")
        for clave, valor in juego.items():
            print(f"{clave}: {valor}")

while True:
    print("\nMENU:")
    print("1). Buscar juego por nombre")
    print("2). Listar juegos disponibles")
    print("3). Listar juegos ordenados por precio descendente")
    print("4). Lista juegos  ordenados Alfabeticamente")
    print("5). Mostrar nombre y el precio del juego más barato.")
    print("6). Crear un string a partir de la lista con el mismo formato")
    print("7). Crear un diccionario con los juegos cuyo precio sea menor de X")

    opcion=input("introduzca una opción: ")

# PARA LISTA-DICCIONARIO
#     if opcion=="1":
#         nombreJuego=input("Introduce el nombre del juego: ")
#         juegoEncontrado=buscarJuegoNombre(nombreJuego, listaJuegos)
#         if juegoEncontrado:
#             print(juegoEncontrado)
#         else:
#             print("No existe el juego")
#
#     elif opcion=="2":
#         listaDisponibles=listarJuegosDisponibles(listaJuegos)
#         print(listaDisponibles)
#
#     elif opcion=="3":
#         listaJuegosOrdenados=mostrarNombrePrecioDesc(listaJuegos)
#
#     elif opcion=="4":
#         mostrarJuegosAlfabetico(listaJuegos)
#
#     elif opcion=="5":
#         mostrarJuegoBarato(listaJuegos)
#
#     elif opcion=="6":
#         pass
#
#     elif opcion=="7":
#         minPrecio=float(input("Cual es el precio limite? "))
#         nuevoDiccionario=crearDiccionario(minPrecio, listaJuegos)
#         print(nuevoDiccionario)
#
#     else:
#         print("Opcion no valida")

# PARA DICCIONARIO-DICCIONARIO
    if opcion =="1":
        nombreJuego=input("Ingrese el nombre del juego: ")
        juegoEncontrado=buscarJuegoNombre(nombreJuego,diccJuegos)
        print(juegoEncontrado)