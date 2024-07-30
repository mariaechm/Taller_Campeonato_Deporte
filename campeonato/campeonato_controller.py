from campeonato import Campeonato

class CampeonatoController:
    def __init__(self):
        self.campeonatos = []

    def agregar_campeonato(self, campeonato):
        if isinstance(campeonato, Campeonato):
            self.campeonatos.append(campeonato)

    def __str__(self):
        campeonatos = "\n".join(str(c) for c in self.campeonatos)
        return f"Campeonatos:\n{campeonatos}"
