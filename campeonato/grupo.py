class Grupo:
    def __init__(self, nombre, numero_equipos):
        self.nombre = nombre
        self.estado_de_partidos = False
        self.numero_equipos = numero_equipos
        self.partidos = []

    def listar_partidos(self):
        return self.partidos

    def __str__(self):
        return f"Grupo: {self.nombre}, Número de Equipos: {self.numero_equipos}"
