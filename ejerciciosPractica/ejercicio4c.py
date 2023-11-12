# Mostrar el alumno con mayor nota y el alumno con menor nota.

notas={

    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

print("El alumno con mayor nota es",(max(notas, key=notas.get)),
      "y el de menor nota es",(min(notas, key=notas.get)))

# # -------------------------------------------------------------

maxAlumno= max(notas, key=notas.get)
maxNota=notas[maxAlumno]
print(f"El alumno con mayor nota es {maxAlumno} con un {maxNota}")

minAlumno= min(notas, key=notas.get)
minNota=notas[minAlumno]
print(f"El alumno con mayor nota es {minAlumno} con un {minNota}")
