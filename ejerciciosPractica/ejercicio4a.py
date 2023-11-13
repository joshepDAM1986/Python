# EJERCICIO 4
# Imagina que estás desarrollando un programa para una escuela que necesita gestionar las notas de los alumnos. La
# escuela nos proporciona las siguiente notas de ejemplo:

# María => 7.9
# Carlos => 9.2
# Pedro => 5.2
# Isabel => 4.7
# Luis =>3.9
# Miguel => 6.0

# Se te pide programar las siguientes funcionalidades usando diccionarios:
#  Hacer la media de todos los alumnos.
#  Buscar un alumno por nombre y nos muestre su nota media, si no existe el alumno mostrar un mensaje informativo.
#  Mostrar el alumno con mayor nota y el alumno con menor nota.
#  Crear otro diccionario con solo los aprobados.
#  Mostrar los nombres de los alumnos de menor a mayor.

notas={

    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

#  Hacer la media de todos los alumnos.
sumaNotas= sum(notas.values())
numAlumnos=len(notas)
mediaTotal= sumaNotas/numAlumnos
print(f"La media total de clase es {round(mediaTotal,2)}")