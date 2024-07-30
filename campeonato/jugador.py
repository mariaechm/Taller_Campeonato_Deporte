from persona import Persona

class Jugador(Persona):
    def __init__(self, id, nombre_completo, fecha_nacimiento, sexo, categoria, peso, altura, numero_goles=0):
        super().__init__(id, nombre_completo, fecha_nacimiento, sexo)
        self.categoria = categoria
        self.peso = peso
        self.altura = altura
        self.numero_goles = numero_goles
        self.estado_fisico = 100

    def ganar_puntos(self):
        pass

    def anotar_gol(self):
        self.numero_goles += 1

    def registrar_lesion(self, tiempo_recuperacion):
        self.estado_fisico -= tiempo_recuperacion

    def __str__(self):
        return f"{super().__str__()}, Categoria: {self.categoria}, Goles: {self.numero_goles}"
