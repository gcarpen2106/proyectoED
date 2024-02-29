from modulos import LeerPartidos, impClasificacion, Equipos, InfoEquipos

datosliga = 'liga.csv'

liga = LeerPartidos()

print("Partidos:")

impClasificacion(liga)