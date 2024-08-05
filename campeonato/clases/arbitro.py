class Arbitro:
    def __init__(self, id_arbitro, nombre_completo, nacionalidad):
        self.id_arbitro = id_arbitro
        self.nombre_completo = nombre_completo
        self.nacionalidad = nacionalidad

    def __str__(self):
        return self.nombre_completo
