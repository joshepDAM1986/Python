# Mostrar el alumno con mayor nota y el alumno con menor nota.

notas={

    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

def alumnoMaxMin():
    maxAlumno= max(notas, key=notas.get) # Guarda la clave del diccionario con mayor valor (nombre del alumno con mas nota)
    maxNota= notas[maxAlumno] # Guarda el valor de la clave guardado antes (la nota del alumno con mayor nota)
    minAlumno = min(notas, key=notas.get)
    minNota = notas[minAlumno]
    return(f"El alumno con mayor nota es {maxAlumno} con un {maxNota}\n"
           f"El alumno con mayor nota es {minAlumno} con un {minNota}")
print(alumnoMaxMin())


