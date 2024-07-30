class Partido:
    def __init__(self, equipoA, equipoB, fecha, hora, ubicacion):
        self.equipoA = equipoA
        self.equipoB = equipoB
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion
        self.resultado = None
        self.ganador = None

    def registrarResultado(self, golesA, golesB):
        self.resultado = (golesA, golesB)
        if golesA > golesB:
            self.ganador = self.equipoA
        elif golesB > golesA:
            self.ganador = self.equipoB
        else:
            self.ganador = 'Empate'
