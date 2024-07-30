class Resultado:
    def __init__(self, goles_equipo_a, goles_equipo_b):
        self.goles_equipo_a = goles_equipo_a
        self.goles_equipo_b = goles_equipo_b
        self.ganador = None
        self.actualizar_resultado(goles_equipo_a, goles_equipo_b)

    def actualizar_resultado(self, goles_a, goles_b):
        self.goles_equipo_a = goles_a
        self.goles_equipo_b = goles_b
        if goles_a > goles_b:
            self.ganador = "Equipo A"
        elif goles_b > goles_a:
            self.ganador = "Equipo B"
        else:
            self.ganador = "Empate"

    def __str__(self):
        return f"Resultado: {self.goles_equipo_a} - {self.goles_equipo_b}, Ganador: {self.ganador}"
