import csv

def Equipos(datosliga):
    equipos = []
    with open(datosliga, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            equipos.append(row['Team 1'])
            
    return equipos

