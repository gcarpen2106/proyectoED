import csv

def LeerPartidos():
    lista = []
    with open ("liga.csv","r") as fichero:
        contenido = csv.DictReader(fichero, delimiter=",")
        next(contenido)

        for i in contenido:
            lista.append(i)
    return lista