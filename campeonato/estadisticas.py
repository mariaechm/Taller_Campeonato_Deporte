class Estadisticas:
    def __init__(self, equipo):
        self.equipo = equipo
        self.puntos = 0
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.goles_favor = 0
        self.goles_contra = 0

    def actualizarEstadisticas(self, goles_favor, goles_contra):
        self.partidos_jugados += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
        if goles_favor > goles_contra:
            self.puntos += 3
            self.partidos_ganados += 1
        elif goles_favor == goles_contra:
            self.puntos += 1
            self.partidos_empatados += 1
        else:
            self.partidos_perdidos += 1
