class Posicion:
    def __init__(self, equipo: str, puntos: int = 0, partidos_ganados: int = 0, partidos_perdidos: int = 0, partidos_empatados: int = 0, diferencia_goles: int = 0):
        self.equipo = equipo
        self.puntos = puntos
        self.partidos_ganados = partidos_ganados
        self.partidos_perdidos = partidos_perdidos
        self.partidos_empatados = partidos_empatados
        self.diferencia_goles = diferencia_goles

    def actualizar_posicion(self, goles_favor: int, goles_contra: int):
        self.diferencia_goles += (goles_favor - goles_contra)
        if goles_favor > goles_contra:
            self.puntos += 3
            self.partidos_ganados += 1
        elif goles_favor < goles_contra:
            self.partidos_perdidos += 1
        else:
            self.puntos += 1
            self.partidos_empatados += 1
