class Campeonato:
    def __init__(self, id_campeonato, nombre, fecha_inicio, fecha_fin, tipo):
        self.id_campeonato = id_campeonato
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo
        self.equipos = []
        self.partidos = []

    def agregarEquipo(self, equipo):
        self.equipos.append(equipo)

    def organizarPartido(self, partido):
        self.partidos.append(partido)

    def getEstadisticas(self):
        estadisticas = []
        for equipo in self.equipos:
            estadisticas.append({
                'equipo': equipo.nombre,
                'puntos': equipo.puntos,
                'goles_a_favor': equipo.goles_a_favor,
                'goles_en_contra': equipo.goles_en_contra,
                'diferencia_goles': equipo.getDiferenciaGoles()
            })
        estadisticas.sort(key=lambda x: x['puntos'], reverse=True)
        return estadisticas

    def getEstadisticasIndividuales(self):
        estadisticas = []
        for equipo in self.equipos:
            for jugador in equipo.jugadores:
                estadisticas.append(jugador.getEstadisticas())
        estadisticas.sort(key=lambda x: x['goles'], reverse=True)
        return estadisticas

    def getCampeon(self):
        if self.equipos:
            campeon = max(self.equipos, key=lambda equipo: equipo.puntos)
            return campeon.nombre
        return None

