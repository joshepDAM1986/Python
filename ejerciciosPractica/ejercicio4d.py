#  Crear otro diccionario con solo los aprobados.

notas = {
    "Maria": 7.9,
    "Carlos": 9.2,
    "Pedro": 5.2,
    "Isabel": 4.7,
    "Luis": 3.9,
    "Miguel": 6.0
}

aprobados = {alumno: media for (alumno, media) in notas.items() if media >= 5}

print(f"aprobados = {aprobados}")
