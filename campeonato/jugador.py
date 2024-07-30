from persona import Persona

class Jugador(Persona):
    def __init__(self, nombre, id, fecha_nacimiento, sexo, categoria, peso, numero_camisa):
        super().__init__(nombre, id, fecha_nacimiento, sexo)
        self.categoria = categoria
        self.peso = peso
        self.numero_camisa = numero_camisa
        self.faltas = 0
        self.estado_fisico = 100
        self.numero_goles = 0
        self.partidos_jugados = 0

    def anotarGol(self):
        self.numero_goles += 1

    def registrarLesion(self, tiempo_recuperacion):
        self.estado_fisico -= tiempo_recuperacion
