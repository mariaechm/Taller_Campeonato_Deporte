from equipo import Equipo
from grupo import Grupo
from partido import Partido
from tabla_posicion import TablaPosicion

class Campeonato:
    def __init__(self, nombre, tipo, premio):
        self.nombre = nombre
        self.tipo = tipo
        self.premio = premio
        self.jugadores = []
        self.equipos = []
        self.partidos = []
        self.grupos = []
        self.tabla_posicion = TablaPosicion()

    def inscribir_equipo(self, equipo):
        if isinstance(equipo, Equipo):
            self.equipos.append(equipo)

    def organizar_grupos(self):
        pass

    def programar_partidos(self):
        pass

    def publicar_resultados(self):
        pass

    def __str__(self):
        equipos = "\n".join(str(e) for e in self.equipos)
        return f"Campeonato: {self.nombre}, Tipo: {self.tipo}, Premio: {self.premio}\nEquipos:\n{equipos}"
