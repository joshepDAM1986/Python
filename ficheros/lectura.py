try:
    f = open("nombrado.txt", "r")
except FileNotFoundError:
    print("El fichero no existe")
except IOError:
    print("Error entrada/salida")
else:
    contenido = f.read()
    print(contenido)
    f.close()