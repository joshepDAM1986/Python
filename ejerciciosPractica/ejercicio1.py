# EJERCICIO 1:
# En una escuela, se ha establecido un sistema de reconocimientos progresivos para los estudiantes basado en su
# rendimiento académico. El sistema se divide en tres categorías y se asigna un porcentaje específico de reconocimiento
# en cada una de ellas que se traduce en dinero sobre lo que pago por su matricula al iniciar el curso academico. Las
# categorías y los porcentajes son los siguientes:
#     Categoría A: Rendimiento sobresaliente (notas de 9 o más): 15% de reconocimiento sobre el precio de su matricula
#     Categoría B: Rendimiento notable (notas de 7 a 8.9): 10% de reconocimiento sobre el precio de su matricula
#     Categoría C: Rendimiento satisfactorio (notas de 5 a 6.9): 5% de reconocimiento sobre el precio de su matricula
# Dada la nota y el precio que un alumno pago por su matricula calcular el dinero que recibe un alumno en funcion de su
# rendimiento.

notaAlumno=0.0
reconocimiento=0.0
categoria=""


notaAlumno = float(input("Ingrese la nota del alumno: "))
if notaAlumno <0 or notaAlumno >10:
    print("La nota no puede ser menor de cero ni mayor de 10")
precioMatricula = float(input("Ingrese el precio de la matrícula: "))
if precioMatricula <0:
    print("El precio de la matricula no puede ser negativo")

if (notaAlumno >= 9):
    reconocimiento = 0.15 * precioMatricula
    categoria = "A"
    print(f"El alumno pertenece a la categoría {categoria} y recibe {reconocimiento}€ como reconocimiento.")
elif notaAlumno < 9 and notaAlumno >= 7:
    reconocimiento = 0.10 * precioMatricula
    catergoria = "B"
    print(f"El alumno pertenece a la categoría {categoria} y recibe {reconocimiento}€ como reconocimiento.")
elif notaAlumno < 7 and notaAlumno >= 5:
    reconocimiento = 0.05 * precioMatricula
    categoria = "C"
    print(f"El alumno pertenece a la categoría {categoria} y recibe {reconocimiento}€ como reconocimiento.")
else:
    categoria=("suspenso")
    print(f"El alumno esta {categoria}")
