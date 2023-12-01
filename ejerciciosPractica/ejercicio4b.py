notas={
    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

# Buscar un alumno por nombre y nos muestre su nota media, si no existe el alumno mostrar un mensaje informativo.
def mostrarMediasAlumno():
    alumno = input("Ingresa el nombre del alumno: ")
    media=notas.get(alumno, "No existe ese alumno")
    return media
print(mostrarMediasAlumno())
