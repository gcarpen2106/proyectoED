from modulos import Equipos

datosliga = 'liga.csv'
equipos = Equipos(datosliga)
print(equipos)


from modulos import LeerPartidos, impClasificacion


liga = LeerPartidos()

impClasificacion(liga)

from modulos import LeerPartidos


liga = LeerPartidos()