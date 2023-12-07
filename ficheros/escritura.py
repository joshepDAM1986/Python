f=open("nombres.txt", "w") # escribe en el archivo sustituyendo
f=open("nombres.txt", "a") # escribe en el archivo añadiendo

nombre="Natalia Chica"

f.write("Jaime Molina\n")
f.write("David Delgado\n")
f.write(f"{nombre} es una alumna de 2ºDAM\n")
f.close()

