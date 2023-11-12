



# EJERCICIO 3:
# Realizar un programa que genere contraseñas aleatorias. El programa pide cuantas contraseñas se van generar y
# después la longitud de las mismas. Los caracteres admitidos en las contraseñas son:
# 0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz

# numContraseñas=int(input("Ingrese el numero de contraeñas: "))
# longContraseñas=int(input("Ingrese cuan larga será la contraseña: "))
# cadena="0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz"
#
# for i in range(numContraseñas):
#     contContraseña = i + 1
#     resultado = ""
#     for i in range(longContraseñas):
#         resultado += random.choice(cadena)
#     print(f"Contraseña {contContraseña}: {resultado}")


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

# Buscar un alumno por nombre y nos muestre su nota media, si no existe el alumno mostrar un mensaje informativo.
# alumno=input("Ingresa el nombre del alumno: ")

# for (clave, valor) in notas.items():
#     if clave == alumno:
#         print(f"{clave}: {valor}")
#         break
# else:
#      print("No existe ese alumno")

#  Mostrar los nombres de los alumnos de menor a mayor.
# listAlumnos=sorted(notas, key=notas.get)
# cadAlumnos="\n".join(listAlumnos)
# print(cadAlumnos)

#  Mostrar el alumno con mayor nota y el alumno con menor nota.
# print("El alumno con mayor nota es",(max(notas, key=notas.get)),
#       "y el de menor nota es",(min(notas, key=notas.get)))

# # -------------------------------------------------------------

# maxAlumno= max(notas, key=notas.get)
# maxNota=notas[maxAlumno]
# print(f"El alumno con mayor nota es {maxAlumno} con un {maxNota}")
#
# minAlumno= min(notas, key=notas.get)
# minNota=notas[minAlumno]
# print(f"El alumno con mayor nota es {minAlumno} con un {minNota}")
