libros = {
    'The Shining': 5.50,
    'Harry Potter and the Goblet of Fire': 10.00,
    '1984': 4.35,
    'The Lord of the Rings':14.99,
    'The Diary of Ana Frank': 24.99
  }

def libroMasCaro():
    libroCaro = max(libros, key=libros.get)
    precioLibro = libros[libroCaro]
    return (f"{libroCaro}")
print(libroMasCaro())


def precioLibros():
    precioTotal = 0.0
    nuevoPrecio={}
    for elemento, valor in libros.items():
        valor=round(valor+(valor*10/100),2)
        libro=elemento
        nuevoPrecio[libro]=valor
    return nuevoPrecio
print(precioLibros())


librosOrdenados=precioLibros()
def diccOrdenado():
    librosListados = ""
    for titulo, precio in sorted(librosOrdenados.items()):
        librosListados += f'Título: {titulo.upper()} | Precio: ${precio}\n'
    return librosListados
print(diccOrdenado())

