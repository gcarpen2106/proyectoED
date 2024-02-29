def InfoEquipos(datosliga, equipos):
    info_equipos = []

    for equipo in equipos:

        ganados = 0
        empatados = 0
        perdidos = 0
        puntos = 0

        for partido in datosliga:

            if partido['Team 1'] == equipo: #Comprobamos que el equipo 1 este dentro de los equipos

                if partido['FT'][0] > partido['FT'][2]:   # Comprobamos que el equipo 1 ha ganado al equipo 2 para ello utilizamos la columna FT si la posicion 0 que los goles anotado por el 
                                                          # equipo 1 es mayor a posicion 2 de la columna FT que son los goles del otro equipo pues realizamos la suma.
                    ganados += 1
                    puntos += 3

                elif partido['FT'][0] == partido['FT'][2]:  # Comprobamos que el equipo 1 ha empatado al equipo 2 para ello utilizamos la columna FT si la posicion 0 que los goles anotado por el 
                                                            # equipo 1 es igual a posicion 2 de la columna FT que son los goles del otro equipo pues realizamos la suma.
                    empatados += 1
                    puntos += 1
                else:  # Si no es nada de esto pues a perdido el equipo 1
                    perdidos += 1

            elif partido['Team 2'] == equipo: #Comprobamos que el equipo 2 este dentro de los equipos
                if partido['FT'][0] < partido['FT'][2]:  # Comprobamos que el equipo 2 ha ganado al equipo 1 para ello utilizamos la columna FT si la posicion 0 que los goles anotado por el 
                                                         # equipo 2 es mayor a posicion 1 de la columna FT que son los goles del otro equipo pues realizamos la suma.
                    ganados += 1
                    puntos += 3

                elif partido['FT'][0] == partido['FT'][2]:  # Comprobamos que el equipo 2 ha empatado al equipo 1 para ello utilizamos la columna FT si la posicion 0 que los goles anotado por el 
                                                            # equipo 2 es igual a posicion 1 de la columna FT que son los goles del otro equipo pues realizamos la suma.
                    empatados += 1
                    puntos += 1
                else:  # Si no es nada de esto pues a perdido el equipo 2
                    perdidos += 1

        info_equipos.append((equipo, ganados, empatados, perdidos, puntos))
    return info_equipos


def Equipos(datosliga):
    equipos = []
    with open(datosliga, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            equipos.append(row['Team 1'])
            
    return equipos

def impClasificacion(liga):
    for i in liga:
        print(i)

import csv

def LeerPartidos():
    lista = []
    with open ("liga.csv","r") as fichero:
        contenido = csv.DictReader(fichero, delimiter=",")
        next(contenido)

        for i in contenido:
            lista.append(i)
    return lista