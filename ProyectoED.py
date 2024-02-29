from modulos import LeerPartidos, impClasificacion, Equipos, InfoEquipos

datosliga = 'liga.csv'

liga = LeerPartidos()

impClasificacion(liga)

equipos = Equipos(datosliga)

info = InfoEquipos(liga,equipos)

print("\n")

print(equipos)