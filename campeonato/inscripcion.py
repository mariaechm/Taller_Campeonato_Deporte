class Inscripcion:
    def __init__(self):
        self.equipos = []

    def inscribirEquipo(self, equipo):
        self.equipos.append(equipo)

    def listarEquipos(self):
        return self.equipos
