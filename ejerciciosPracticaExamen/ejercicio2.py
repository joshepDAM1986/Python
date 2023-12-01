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

def mostrar(lista):
    for i in range(0, len(lista)):
        print("posicion",i,":",lista[i])
def modificar(lista):
    for i in range(0, len(lista)):
        lista[i]*=2
    return lista
def longitud(lista):
    return len(lista)

funciones ={
    "mostrar":mostrar,
    "modificar":modificar,
    "longitud":longitud
}

seleccion=(funciones.get(opcion.lower(), lambda x:"error"))
print(seleccion(lista))