# Mostrar los nombres de los alumnos de menor a mayor.

notas={

    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

listAlumnos=sorted(notas, key=notas.get)
cadAlumnos="\n".join(listAlumnos)
print(cadAlumnos)