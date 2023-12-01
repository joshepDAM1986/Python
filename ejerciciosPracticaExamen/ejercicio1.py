opcion=input("¿Que tipo de comida quieres? ")

# if opcion.lower()=="fruta":
#     res="manzana, platano o pera"
# elif opcion.lower()=="verdura":
#     res="tomate, lechuga o zanahoria"
# elif opcion.lower()=="carne":
#     res="cerdo, ternera o pollo"
# elif opcion.lower()=="pescado":
#     res="sardina, caballa o salmonete"
# else:
#     res="no tenemos ese tipo de comida"

# print(res)

tipoComida= {
    "fruta":"manzana, platano o pera",
    "verdura":"tomate, lechuga o zanahoria",
    "carne":"cerdo, ternera o pollo",
    "pescado":"sardina, caballa o salmonete"
}

seleccion=(tipoComida.get(opcion.lower(),"No tenemos este tipo de comida"))
print(seleccion)