from jugador import Jugador
from equipo import Equipo
from campeonato import Campeonato

class InputView:
    def obtener_datos_campeonato(self):
        nombre = input("Ingrese el nombre del campeonato: ")
        tipo = input("Ingrese el tipo de campeonato: ")
        premio = input("Ingrese el premio del campeonato: ")
        return Campeonato(nombre, tipo, premio)

    def obtener_datos_equipo(self):
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        equipo = Equipo(nombre_equipo)
        while True:
            agregar_jugador = input("¿Desea agregar un jugador? (s/n): ")
            if agregar_jugador.lower() == 's':
                id = input("ID del jugador: ")
                nombre_completo = input("Nombre completo del jugador: ")
                fecha_nacimiento = input("Fecha de nacimiento del jugador: ")
                sexo = input("Sexo del jugador: ")
                categoria = input("Categoría del jugador: ")
                peso = float(input("Peso del jugador: "))
                altura = float(input("Altura del jugador: "))
                jugador = Jugador(id, nombre_completo, fecha_nacimiento, sexo, categoria, peso, altura)
                equipo.agregar_jugador(jugador)
            else:
                break
        return equipo
