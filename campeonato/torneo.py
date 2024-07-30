from partido import Partido
from estadisticas import Estadisticas

class Torneo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []
        self.partidos = []

    def agregarEquipo(self, equipo):
        self.equipos.append(equipo)

    def programarPartidos(self):
        if len(self.equipos) % 2 == 1:
            self.equipos.append(None)  # Añadir un descanso si es necesario
        rondas = len(self.equipos) - 1
        for ronda in range(rondas):
            for i in range(len(self.equipos) // 2):
                equipoA = self.equipos[i]
                equipoB = self.equipos[-i-1]
                if equipoA and equipoB:
                    partido = Partido(equipoA, equipoB, None, None, None)
                    self.partidos.append(partido)
            self.equipos.insert(1, self.equipos.pop())  # Rotar equipos

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
            if equipo is None:
                continue
            estadisticas = Estadisticas(equipo)
            for partido in self.partidos:
                if partido.equipoA == equipo:
                    estadisticas.actualizarEstadisticas(partido.resultado[0], partido.resultado[1])
                elif partido.equipoB == equipo:
                    estadisticas.actualizarEstadisticas(partido.resultado[1], partido.resultado[0])
            tabla.append(estadisticas)
        tabla.sort(key=lambda x: x.puntos, reverse=True)
        return tabla
