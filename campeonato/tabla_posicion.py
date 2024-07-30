class TablaPosicion:
    def __init__(self):
        self.posiciones = []

    def ordenar_posiciones(self):
        pass

    def actualizar_posiciones(self, equipo, puntos):
        pass

    def __str__(self):
        posiciones = "\n".join(str(p) for p in self.posiciones)
        return f"Tabla de Posiciones:\n{posiciones}"
