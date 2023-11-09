for i in[1,2,3]:
    print(i,end=" ")
print("\n")

for _ in [1,2,3,4,5]:
    print("hola", end=" ")
print("\n")

#for(int i=0;i<100;i++)
for num in range(100):
    print(num,end=" ")
print("\n")

desde=5
hasta=30

for num in range(desde,hasta+1):
    print(num,end=" ")

for letra in "coleta":
    print(letra, end="")
print("\n")

numeros=[5,1,-7,40,23,2,8]

for num in sorted(numeros):
    print(f"su numero es {num}", end=" ")
print("\n")

diasSemana=["lunes","martes","miescoles","jueves","viernes","sabado","domingo"]

for dia in diasSemana:
    print(dia,end=" ")
print("\n")

for i in range(len(diasSemana)):
    print(f"{diasSemana[i]} es el dia numero {i+1}")
finDeSemana=["jupìter","domingo"]

incluido=True

for dia in finDeSemana:
    incluido= dia in diasSemana
print(f"Fin de semana incluido en la semana:{incluido}")

for dia in diasSemana[1:]:
    print(dia)

contenido="""
             nombre,eddad,altura\n
             Fabio,19,1.80\n
             Jesus,19,1.88\n
             Juan Carlos,65,2.02\n
          """
