alumnos= {
    "Maria":7.9,
    "Carlos":9.2,
    "Pedro":5.2,
    "Isabel":4.7,
    "Luis":3.9,
    "Miguel":6.0
}

def mediaTotal():
    sumNotas=sum(alumnos.values())
    numAlumnos=len(alumnos)
    media=round((sumNotas/numAlumnos),2)
    return media
print(mediaTotal())

def mediaNotas():
    alumno=input("Escribe el nombre del alumno: ")
    media=(alumnos.get(alumno, "no existe ese alumno"))
    return media
print(mediaNotas())

def mayorMenorNota():
    alumnoMax=max(alumnos, key=alumnos.get)
    maxNota=alumnos[alumnoMax]
    alumnoMin = min(alumnos, key=alumnos.get)
    minNota = alumnos[alumnoMin]
    return (f"El alumno con mayor nota es {alumnoMax} con {maxNota}\n"
            f"El alumno con menor nota es {alumnoMin} con {minNota}")
print(mayorMenorNota())

def diccAprobados():
    nuevoDicc={}
    for clave, valor in alumnos.items():
        if valor>=5:
            nuevoDicc[clave]=valor
    return nuevoDicc
print(diccAprobados())

def nombreOrdMenorMayor():
    listaOrdenada=sorted(alumnos, key=alumnos.get)
    cadenaOrdenada="\n".join(listaOrdenada)
    return cadenaOrdenada
print(nombreOrdMenorMayor())


