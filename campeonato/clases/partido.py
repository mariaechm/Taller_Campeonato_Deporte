class Partido:
    def __init__(self, id_partido, equipo_local, equipo_visitante, fecha, estadio, arbitro):
        self.id_partido = id_partido
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.estadio = estadio
        self.arbitro = arbitro
        self.goles_local = 0
        self.goles_visitante = 0
        self.sanciones = []

    def jugarPartido(self, goles_local, goles_visitante, goleadores_local, goleadores_visitante):
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

        # Actualizar los goles de los jugadores
        for jugador in goleadores_local:
            jugador.goles += 1
        for jugador in goleadores_visitante:
            jugador.goles += 1

        self.equipo_local.goles_a_favor += goles_local
        self.equipo_local.goles_en_contra += goles_visitante
        self.equipo_visitante.goles_a_favor += goles_visitante
        self.equipo_visitante.goles_en_contra += goles_local

        # Actualizar los puntos
        if goles_local > goles_visitante:
            self.equipo_local.puntos += 3
        elif goles_local < goles_visitante:
            self.equipo_visitante.puntos += 3
        else:
            self.equipo_local.puntos += 1
            self.equipo_visitante.puntos += 1

    def agregarSancion(self, sancion):
        self.sanciones.append(sancion)

    def getResultado(self):
        if self.goles_local > self.goles_visitante:
            estado = f"Gano {self.equipo_local.nombre}"
        elif self.goles_local < self.goles_visitante:
            estado = f"Gano {self.equipo_visitante.nombre}"
        else:
            estado = "Empate"
        return f"{self.equipo_local.nombre} {self.goles_local} - {self.goles_visitante} {self.equipo_visitante.nombre} ({estado})\nEstadio: {self.estadio}\nArbitro: {self.arbitro}"
