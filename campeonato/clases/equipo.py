class Equipo:
    def __init__(self, id_equipo, nombre):
        self.id_equipo = id_equipo
        self.nombre = nombre
        self.jugadores = []
        self.goles = 0
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)

    def getGoles(self):
        self.goles = sum(jugador.goles for jugador in self.jugadores)
        return self.goles

    def getDiferenciaGoles(self):
        return self.goles_a_favor - self.goles_en_contra