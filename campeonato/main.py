from clases.arbitro import Arbitro
from clases.sancion import Sancion
from clases.temporada import Temporada
from clases.calendario import Calendario
from clases.estadio import Estadio
from clases.jugador import Jugador
from clases.equipo import Equipo
from clases.partido import Partido
from clases.campeonato import Campeonato
from clases.inscripcion import Inscripcion
from clases.estadisticas import Estadisticas


def main():
    temporada = Temporada(2024)
    campeonato = Campeonato(1, "Campeonato Summer", "2024-08-01", "2024-09-01", "Liga")
    temporada.agregarCampeonato(campeonato)
    calendario = Calendario()

    # Inscripción
    inscripcion = Inscripcion(campeonato)
    inscripcion.inscribirEquipos()

    # Creación de partidos y agregacion al calendario
    num_partidos = int(input("\nNúmero de partidos: "))
    for i in range(num_partidos):
        print("\n ---------------------------------------------------")
        id_partido = i + 1

        while True:
            try:
                nombre_equipo_local = input(" •Nombre del equipo local: ")
                equipo_local = next(equipo for equipo in campeonato.equipos if equipo.nombre == nombre_equipo_local)
                break
            except StopIteration:
                print("Nombre de equipo local no válido. Inténtalo de nuevo.")

        while True:
            try:
                nombre_equipo_visitante = input(" •Nombre del equipo visitante: ")
                equipo_visitante = next(
                    equipo for equipo in campeonato.equipos if equipo.nombre == nombre_equipo_visitante)
                break
            except StopIteration:
                print("Nombre de equipo visitante no válido. Inténtalo de nuevo.")

        fecha = input(" Fecha del partido (YYYY-MM-DD): ")
        estadio = Estadio(i + 1, input(" Nombre del estadio: "), input("Ubicación del estadio: "),
                          int(input(" Capacidad del estadio: ")))
        arbitro = Arbitro(i + 1, input(" Nombre del Arbitro: "), input("Nacionalidad del árbitro: "))

        partido = Partido(id_partido, equipo_local, equipo_visitante, fecha, estadio, arbitro)
        calendario.agregarPartido(partido)
        campeonato.organizarPartido(partido)

    # Jugar los partidos
    for partido in calendario.partidos:
        print("\n---------------------------------------------------")
        print(
            f"Jugar partido {partido.id_partido}: '{partido.equipo_local.nombre}' vs '{partido.equipo_visitante.nombre}'")
        goles_local = int(input(f"Goles de '{partido.equipo_local.nombre}': "))
        goles_visitante = int(input(f"Goles de '{partido.equipo_visitante.nombre}': "))
        print("---------------------------------------------------")

        goleadores_local = []
        for i in range(goles_local):
            while True:
                try:
                    num_camiseta = int(
                        input(f" Número de camiseta del goleador {i + 1} de '{partido.equipo_local.nombre}': "))
                    goleador = next(jugador for jugador in partido.equipo_local.jugadores if
                                    jugador.numero_camiseta == num_camiseta)
                    goleadores_local.append(goleador)
                    break
                except StopIteration:
                    print("Número de camiseta no válido. Inténtalo de nuevo.")
                    print("---------------------------------------------------")

        goleadores_visitante = []
        for i in range(goles_visitante):
            while True:
                try:
                    num_camiseta = int(
                        input(f"Número de camiseta del goleador {i + 1} de '{partido.equipo_visitante.nombre}': "))
                    goleador = next(jugador for jugador in partido.equipo_visitante.jugadores if
                                    jugador.numero_camiseta == num_camiseta)
                    goleadores_visitante.append(goleador)
                    break
                except StopIteration:
                    print("Número de camiseta no válido. Inténtalo de nuevo.")

        partido.jugarPartido(goles_local, goles_visitante, goleadores_local, goleadores_visitante)
        print("---------------------------------------------------")

        # Añadir sanciones
        num_sanciones = int(input("Número de sanciones en este partido: "))
        for s in range(num_sanciones):
            while True:
                try:
                    num_camiseta = int(input(" Número de camiseta del jugador sancionado: "))
                    jugador = next(jugador for jugador in partido.equipo_local.jugadores if
                                   jugador.numero_camiseta == num_camiseta)
                    break
                except StopIteration:
                    print("Número de camiseta no válido. Inténtalo de nuevo.")

            tipo = input(" Tipo de sanción (amarilla/roja/suspensión): ")
            motivo = input(" Motivo de la sanción: ")
            sancion = Sancion(jugador, tipo, partido, motivo)
            partido.agregarSancion(sancion)

    # Imprimir los resultados y estadísticas
    print("\n---------------------------------------------------")
    print("\nResultados de los partidos:")
    print("\n---------------------------------------------------")
    for partido in calendario.partidos:
        print(partido.getResultado())

    estadisticas = Estadisticas(campeonato)
    estadisticas.mostrarEstadisticasEquipos()
    estadisticas.mostrarEstadisticasIndividuales()

    print("\nCampeón del campeonato 🏆:")
    print(campeonato.getCampeon())


if __name__ == "__main__":
    main()
