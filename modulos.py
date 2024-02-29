import csv

def LeerPartidos():
    lista = []
    with open ("liga.csv","r") as fichero:
        contenido = csv.DictReader(fichero, delimiter=",")
        next(contenido)

        for i in contenido:
            lista.append(i)
    return lista

def impClasificacion(liga):
    for i in liga:
        print(i)

