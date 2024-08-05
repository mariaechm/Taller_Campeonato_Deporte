class Estadio:
    def __init__(self, id_estadio, nombre, ubicacion, capacidad):
        self.id_estadio = id_estadio
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion} (Capacidad: {self.capacidad})"
