from equipo import Equipo

class EquipoController:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, equipo):
        if isinstance(equipo, Equipo):
            self.equipos.append(equipo)

    def __str__(self):
        equipos = "\n".join(str(e) for e in self.equipos)
        return f"Equipos:\n{equipos}"
