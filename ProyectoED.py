from modulos import LeerPartidos, impClasificacion, Equipos, InfoEquipos

datosliga = 'liga.csv'

liga = LeerPartidos()

impClasificacion(liga)

equipos = Equipos(datosliga)

print("\n")

print("Equipos:",equipos)

info = InfoEquipos(liga,equipos)

print("\n")

print("Clasificación:",info)