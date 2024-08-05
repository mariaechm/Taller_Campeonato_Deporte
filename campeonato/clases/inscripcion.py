from clases.equipo import Equipo
from clases.jugador import Jugador

class Inscripcion:
    def __init__(self, campeonato):
        self.campeonato = campeonato

    def inscribirEquipos(self):
        num_equipos = int(input("\nNúmero de equipos: "))
        for i in range(num_equipos):
            nombre_equipo = input(f"\n * Nombre del equipo {i + 1}: ")
            equipo = Equipo(i + 1, nombre_equipo)

            print("  ---------------------------------------------------")
            num_jugadores = int(input(f"  Número de jugadores para el equipo '{nombre_equipo}': "))
            for j in range(num_jugadores):
                id_jugador = j + 1
                print("  ---------------------------------------------------")
                nombre_completo = input(f"  Nombre completo del jugador {j + 1}: ")
                fecha_nacimiento = input(f"  Fecha de nacimiento del jugador {j + 1} (YYYY-MM-DD): ")
                sexo = input(f"  Sexo del jugador (masculino/femenino) {j + 1}: ")
                numero_camiseta = int(input(f"  Número de camiseta del jugador {j + 1}: "))
                peso = float(input(f"  Peso del jugador {j + 1} (kg): "))
                estatura = float(input(f"  Estatura del jugador {j + 1} (m): "))

                jugador = Jugador(id_jugador, nombre_completo, fecha_nacimiento, sexo, numero_camiseta, peso, estatura)
                equipo.agregarJugador(jugador)

            self.campeonato.agregarEquipo(equipo)
