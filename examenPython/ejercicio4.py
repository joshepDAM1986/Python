transformar = {
    "int": int,
    "float": float,
    "boolean": eval
}

def es_float(cadena):
    partes = cadena.split(".")
    return (len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit())

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

datos_peliculas="""titulo;genero;minutos;recaudacion;disponible
Los Vengadores;superheroes;140;367.86;True
La Monja;terror;100;123.57;False
El Reino;suspense;90;21.54;False
Scream 3;terror;123;300.12;True
Pulp fiction;drama;150;98.3;False
La liga de la Justicia;superheroes;120;190.12;True"""

lineas = datos_peliculas.split("\n")
cabecera = lineas[0].split(";")
diccPeliculas = {}

for linea in lineas[1:]:
    dato = dict(zip(cabecera, linea.split(";")))
    castear_datos(dato)
    diccPeliculas[dato["titulo"]] = dato

print(diccPeliculas)

def pelisOrdenadas(diccPeliculas):
    pelisOrdenadas = sorted(diccPeliculas.items(), key=lambda x: x[1]["minutos"], reverse=True)

    for titulo, datos in pelisOrdenadas:
        print(f'Título: {titulo}, Duración: {datos["minutos"]}')

def menosRecaudada(diccPeliculas):
    peliMenosRecaudada = min(diccPeliculas.items(), key=lambda x: x[1]["recaudacion"])
    print(f"Pelicula: {peliMenosRecaudada[0]}")

bucle=True
while bucle:
    print("0. Salir")
    print("1. Ordenar")
    print("2. Menos Rentable")
    print("3. Filtro")
    print("4. Exportar")
    opcion = input("Introduzca una opción: ")

    if opcion == "0":
        bucle=False

    elif opcion=="1":
        pelisOrdenadas(diccPeliculas)

    elif opcion=="2":
        menosRecaudada(diccPeliculas)




