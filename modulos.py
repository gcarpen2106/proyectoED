import csv

def quienGana(resultado):
    if resultado[0] > resultado[2]:
        return 1
    elif resultado[0] == resultado[2]:
        return 0
    else:
        return -1
