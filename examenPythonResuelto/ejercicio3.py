# EJERCICIO 3
#
# A partir del fichero ejercicio3.py que contiene un diccionario como el de la captura:
# El programa debe hacer todo lo siguiente:
# a)	(0,5 puntos). Mostrar el título del libro más caro.
# b)	(1 punto). Crear una copia del diccionario con el precio subido un 10% a todos los libros.
# c)	(0,5 puntos). Usando el diccionario creado en el apartado anterior mostrar ordenados alfabeticamente todos los libros uno por cada linea con el siguiente formato:
# Titulo:TITULO EN MAYUSCULAS | Precio:PRECIO DEL LIBRO

libros = {
    'The Shining': 5.50,
    'Harry Potter and the Goblet of Fire': 10.00,
    '1984': 4.35,
    'The Lord of the Rings': 14.99,
    'The Diary of Ana Frank': 24.99
  }

print(max(libros, key=libros.get))

nuevoDic = dict(libros)
for nombre, precio in nuevoDic.items():
    nuevoDic[nombre] = precio+precio*10/100
print(nuevoDic)


ordenado = dict(sorted(nuevoDic.items()))
for nombre , precio in ordenado.items():
    print(f"Titulo: {nombre.upper()} | Precio: {precio}")
