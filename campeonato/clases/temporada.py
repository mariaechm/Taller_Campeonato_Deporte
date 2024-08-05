class Temporada:
    def __init__(self, anio):
        self.anio = anio
        self.campeonatos = []

    def agregarCampeonato(self, campeonato):
        self.campeonatos.append(campeonato)

    def __str__(self):
        return f"Temporada {self.anio}"