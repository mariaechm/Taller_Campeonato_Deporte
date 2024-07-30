from jugador import Jugador

class Equipo:
    def __init__(self, nombre_equipo):
        self.nombre_equipo = nombre_equipo
        self.miembros = []

    def agregar_jugador(self, jugador):
        if isinstance(jugador, Jugador):
            self.miembros.append(jugador)

    def eliminar_jugador(self, jugador):
        if jugador in self.miembros:
            self.miembros.remove(jugador)

    def listar_jugadores(self):
        return self.miembros

    def __str__(self):
        jugadores = "\n".join(str(j) for j in self.miembros)
        return f"Equipo: {self.nombre_equipo}\nJugadores:\n{jugadores}"
