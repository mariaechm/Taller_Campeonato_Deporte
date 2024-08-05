class Calendario:
    def __init__(self):
        self.partidos = []

    def agregarPartido(self, partido):
        self.partidos.append(partido)

    def getPartidosPorFecha(self, fecha):
        return [partido for partido in self.partidos if partido.fecha == fecha]

    def __str__(self):
        return "\n".join([str(partido) for partido in self.partidos])