# i=1
# while i<=10:
#     print(i,end=" ")
#     i+=1
# print("adios")
#
# respuesta=("")
#
# while respuesta.lower()!="si":
#     respuesta=input(("Di que si"))
#     print(f"Has dicho {respuesta}")
# print("Salimos")

opcion=0
while opcion!=3:
    numero1 = int(input("Escribe un numero: "))
    numero2 = int(input("Escribe un numero: "))
    opcion=input("1). Sumar\n2). Restar\n3). Salir\n")
    if int(opcion==1):
        resultado=int(numero1+numero2)
        print(f"El resultado de la suma es {resultado}")
    elif int(opcion==2):
        resultado=int(numero1-numero2)
        print(f"El resultado de la resta es {resultado}")
    else:
        print("Chao Bacalao")