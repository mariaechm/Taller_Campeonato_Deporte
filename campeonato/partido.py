from resultado import Resultado

class Partido:
    def __init__(self, equipo_a, equipo_b, fecha, hora, ubicacion):
        self.equipo_a = equipo_a
        self.equipo_b = equipo_b
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion
        self.resultado = None

    def jugar_partido(self, goles_a, goles_b):
        self.resultado = Resultado(goles_a, goles_b)

    def __str__(self):
        return f"Partido: {self.equipo_a} vs {self.equipo_b} - Fecha: {self.fecha}, Hora: {self.hora}, Ubicación: {self.ubicacion}"
