from partido import Partido
from estadisticas import Estadisticas

class Liga:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []
        self.partidos = []

    def agregarEquipo(self, equipo):
        self.equipos.append(equipo)

    def programarPartidos(self):
        for i, equipoA in enumerate(self.equipos):
            for equipoB in self.equipos[i+1:]:
                partido = Partido(equipoA, equipoB, None, None, None)
                self.partidos.append(partido)

    def registrarResultados(self, resultados):
        for resultado in resultados:
            equipoA, equipoB, golesA, golesB = resultado
            for partido in self.partidos:
                if partido.equipoA == equipoA and partido.equipoB == equipoB:
                    partido.registrarResultado(golesA, golesB)
                    break

    def calcularClasificacion(self):
        tabla = []
        for equipo in self.equipos:
            estadisticas = Estadisticas(equipo)
            for partido in self.partidos:
                if partido.equipoA == equipo:
                    estadisticas.actualizarEstadisticas(partido.resultado[0], partido.resultado[1])
                elif partido.equipoB == equipo:
                    estadisticas.actualizarEstadisticas(partido.resultado[1], partido.resultado[0])
            tabla.append(estadisticas)
        tabla.sort(key=lambda x: x.puntos, reverse=True)
        return tabla
