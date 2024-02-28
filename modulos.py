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

    for equipo in equipos:

        resultados = []
        puntos = 0

        for partido in datosliga:

            if partido['Team 1'] == equipo: 

                resultados.append(quienGana(partido['FT']))

            elif partido['Team 2'] == equipo: 
                
                resultados.append(quienGana(partido['FT']))
            
            puntos = Puntos(resultados)
        
        print(equipo,":",resultados,"(",puntos,")")

def quienGana(resultado):
    if resultado[0] > resultado[2]:
        return 1
    elif resultado[0] == resultado[2]:
        return 0
    else:
        return -1

def Puntos(info):
    puntos = 0

    for punto in info:
        if punto == 1:
            puntos += 3
        elif punto == 0:
            puntos += 1
        else:
            puntos += 0
    
    return puntos