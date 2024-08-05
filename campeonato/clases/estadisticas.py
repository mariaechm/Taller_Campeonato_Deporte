from tabulate import tabulate

class Estadisticas:
    def __init__(self, campeonato):
        self.campeonato = campeonato

    def mostrarEstadisticasEquipos(self):
        estadisticas = self.campeonato.getEstadisticas()
        print("\nEstadísticas de equipos:")
        print("\n------------------------------------------------")
        print(tabulate(estadisticas, headers="keys"))

    def mostrarEstadisticasIndividuales(self):
        estadisticas_individuales = self.campeonato.getEstadisticasIndividuales()
        print("\nEstadísticas individuales:")
        print("\n------------------------------------------------")
        print(tabulate(estadisticas_individuales, headers="keys"))