class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregarJugador(self, jugador):
        self.miembros.append(jugador)

    def eliminarJugador(self, jugador):
        self.miembros.remove(jugador)

    def listarJugadores(self):
        return self.miembros
