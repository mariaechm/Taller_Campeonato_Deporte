class Persona:
    def __init__(self, id, nombre_completo, fecha_nacimiento, sexo):
        self.id = id
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo

    def __str__(self):
        return f"{self.nombre_completo} (ID: {self.id}, Fecha de Nacimiento: {self.fecha_nacimiento}, Sexo: {self.sexo})"
