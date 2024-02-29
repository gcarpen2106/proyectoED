import csv

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
