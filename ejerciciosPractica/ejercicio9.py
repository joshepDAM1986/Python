opcion=input("¿quieres mostrar, modificar o longitud? ")
lista=[4,8,14,22]

# if opcion=="mostrar":
#     for i in range(0,len(lista)):
#         print("posicion",i,":",lista[i])
# elif opcion=="modificar":
#     for i in range(0,len(lista)):
#         lista[i]*=2
#     print(lista)
# elif opcion=="longitud":
#     print(len(lista))
# else:
#     print("error")

def funMostrar(lista):
    for i in range(0, len(lista)):
        resultado="posicion", i, ":", lista[i]
        return resultado
def funModificar(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2
    return lista

def funLongitud(lista):
    return len(lista)

funciones = {
    "mostrar":funMostrar,
    "modificar":funModificar,
    "longitud":funLongitud
}

seleccion= funciones.get(opcion.lower(), lambda x:"error")
if opcion.lower()=="mostrar":
    seleccion(lista)
else:
    print(seleccion(lista))
