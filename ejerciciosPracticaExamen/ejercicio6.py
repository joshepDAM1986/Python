frutas= {
    "Platano":1.35,
    "Manzana":1.80,
    "Pera":0.85,
    "Naranja":0.7
}

def comprarKilos():
    precioTotal=0
    numKilos= int(input("Ingrese el numero de kilos que comprar: "))
    for clave, valor in frutas.items():
        precio=round((numKilos*valor),2)
        fruta=clave
        precioTotal+=precio
        print(f"{fruta}:{precio}")
    valorPrecioTotal= f"Precio total a pagar: {precioTotal}"
    return valorPrecioTotal
print(comprarKilos())

def frutaBarata():
    minFruta=min(frutas, key=frutas.get)
    return minFruta
print(frutaBarata())

def frutasOrdMaxMin():
    frutasOrdenadas=dict(sorted(frutas.items(), key=lambda x:x[1], reverse=True))
    return frutasOrdenadas
print(frutasOrdMaxMin())

def frutasCaras():
    precio=0
    diccFrutasCaras={}
    for clave, valor in frutas.items():
        if valor > 1:
            diccFrutasCaras[clave]=valor
    return diccFrutasCaras
print(frutasCaras())




