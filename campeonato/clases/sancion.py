class Sancion:
    def __init__(self, jugador, tipo, partido, motivo):
        self.jugador = jugador
        self.tipo = tipo 
        self.partido = partido
        self.motivo = motivo

    def __str__(self):
        return f"{self.tipo} para {self.jugador.nombre_completo} en el partido {self.partido.id_partido} - Motivo: {self.motivo}"
