# Mostrar los nombres de los alumnos de menor a mayor.

notas={

    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

def nombresAlumnosOrdenados():
    listAlumnos=sorted(notas, key=notas.get) # guarda una lista ordenada con los nombre ordenados de menor a mayor por nota
    cadAlumnos=" ".join(listAlumnos) # guarda un string con el contenido de la lista separados por espacios
    return cadAlumnos # muestra el string obtenido
print(nombresAlumnosOrdenados())