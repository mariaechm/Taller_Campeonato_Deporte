from datetime import date, datetime

class Jugador:
    def __init__(self, id_jugador, nombre_completo, fecha_nacimiento, sexo, numero_camiseta, peso, estatura):
        self.id_jugador = id_jugador
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_camiseta = numero_camiseta
        self.peso = peso
        self.estatura = estatura
        self.goles = 0

    def getEdad(self):
        hoy = date.today()
        nacimiento = datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d')
        return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))

    def getEstadisticas(self):
        return {
            'nombre': self.nombre_completo,
            'goles': self.goles,
            'edad': self.getEdad(),
            'peso': self.peso,
            'estatura': self.estatura
        }
