notas={

    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

# Buscar un alumno por nombre y nos muestre su nota media, si no existe el alumno mostrar un mensaje informativo.

def buscarAlumnoNombre():
    alumno=input("Ingresa el nombre del alumno: ")
    for (clave, valor) in notas.items():
        if clave == alumno:
            return(f"{clave}: {valor}")
        else:
            return("No existe ese alumno")

print(buscarAlumnoNombre())
