# print("Ejemplo","09-10-2023","Siguiente día", sep=" | ", end=" ")
# print("Siguiente día")
#
# edad=18.5
# nombre="Jaime"
#
# print(nombre, edad)
# print(type(nombre), type(edad))
#
# PI=3.14159242
# radio=5
#
# total=PI*radio+radio+2*PI*radio
#
# print(total)

# print("""Esto es para escribir un string que tenga varias líneas"
#       y que respete el espacio y los tabuladores,
#       como por ejemplo esto de      aquí""")
#
# parrafo="""Esto es para escribir un string que tenga varias líneas"
#       y que respete el espacio y los tabuladores,
#       como por ejemplo esto de      aquí"""
#
# print(parrafo)
#
# print(1/3)
# print(1//3)


# a,b=6,14
# nombre1,nombre2="Pepe","Paco"
# nombre,edad="Ana",25
#
# print(a,b)
# print(nombre1,nombre2)
# print(nombre,edad)

# aux=a
# a=b
# b=aux
# print(a,b)

# Es lo mismo que

# a,b=b,a
# print(a,b)
#
# nombre,edad = edad,nombre
#
# numero=0
# numero+=1
# numero-=7
# numero*=2
#
# coche="BMW"
# precio=50000.99
# print(coche," vale ",str(precio)*2)
#
# numero1=4.6781
# numero2=1.434
#
# print(round(numero1,2))
# print(round(numero1,6))
# print(round(numero2,2))
# print(round(numero2,0))
#
# ------------------------------------------------------------------------------------------------------
# juego="warhamer"
# version=40000
#
# print("El juego "+ juego + " va por la versión " +str(version) +" y en adelante")
# ======================================================================================================
# frase="El juego "+ juego + " va por la versión " +str(version) +" y en adelante"
# print(frase)
# ======================================================================================================
# frase=f"El juego {juego} va por la version {version} y en adelante"
# print(frase)
# ------------------------------------------------------------------------------------------------------

# Booleanos
x=3
print(0<x<=4)
print(3>=x>=1)
print(1<=x>=4)
print(2>x>5) # Esto no es posible pero lo evalua igualmente
print(x==3)
print(1<x==3)

x=6
print(x<2 and x>5) # &&
print(x<2 or x>5) # ||
print(not(x>5))

# Función imput
nombre=input("Su nombre es:")
print(f"Usted se llama {nombre}")

edad=int(input("Su edad es:"))
print(f"Dentro de 10 años tendrá {edad+10} años de edad")