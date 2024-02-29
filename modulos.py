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

def Equipos(datosliga):
    equipos = []
    with open(datosliga, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            equipos.append(row['Team 1'])
            
    return set(equipos)

def InfoEquipos(datosliga, equipos):
    info_equipos = []
    datos = []