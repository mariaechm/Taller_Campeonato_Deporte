from equipo import Equipo
from jugador import Jugador
from liga import Liga
from torneo import Torneo
from grupo import Grupo
from partido import Partido

def crear_jugador():
    nombre = input("Nombre del jugador: ")
    id = input("ID del jugador: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input("Sexo (M/F): ").strip().lower() == 'm'
    categoria = input("Categoría del jugador: ")
    peso = float(input("Peso del jugador: "))
    numero_camisa = int(input("Número de camisa: "))
    return Jugador(nombre, id, fecha_nacimiento, sexo, categoria, peso, numero_camisa)

def crear_equipo():
    nombre_equipo = input("Nombre del equipo: ")
    equipo = Equipo(nombre_equipo)
    num_jugadores = int(input(f"¿Cuántos jugadores tiene {nombre_equipo}? "))
    for _ in range(num_jugadores):
        jugador = crear_jugador()
        equipo.agregarJugador(jugador)
    return equipo

def seleccionar_tipo_campeonato():
    print("Selecciona el tipo de campeonato:")
    print("1. Liga")
    print("2. Torneo")
    print("3. Grupo")
    opcion = int(input("Opción (1/2/3): "))
    if opcion == 1:
        return "liga"
    elif opcion == 2:
        return "torneo"
    elif opcion == 3:
        return "grupo"
    else:
        print("Opción no válida. Seleccionando 'Liga' por defecto.")
        return "liga"

def registrar_resultados(partidos):
    resultados = []
    for partido in partidos:
        print(f"Partido: {partido.equipoA.nombre} vs {partido.equipoB.nombre}")
        golesA = int(input(f"Goles de {partido.equipoA.nombre}: "))
        golesB = int(input(f"Goles de {partido.equipoB.nombre}: "))
        resultados.append((partido.equipoA, partido.equipoB, golesA, golesB))
    return resultados

def main():
    num_equipos = int(input("¿Cuántos equipos van a participar? "))
    equipos = []
    for _ in range(num_equipos):
        equipo = crear_equipo()
        equipos.append(equipo)

    tipo_campeonato = seleccionar_tipo_campeonato()
    nombre_campeonato = input("Nombre del campeonato: ")

    if tipo_campeonato == "liga":
        campeonato = Liga(nombre_campeonato)
    elif tipo_campeonato == "torneo":
        campeonato = Torneo(nombre_campeonato)
    elif tipo_campeonato == "grupo":
        campeonato = Grupo(nombre_campeonato)

    for equipo in equipos:
        campeonato.agregarEquipo(equipo)

    campeonato.programarPartidos()
    resultados = registrar_resultados(campeonato.partidos)
    campeonato.registrarResultados(resultados)

    clasificacion = campeonato.calcularClasificacion()
    print("\nClasificación final:")
    for estadisticas in clasificacion:
        print(f"Equipo: {estadisticas.equipo.nombre}, Puntos: {estadisticas.puntos}")

if __name__ == "__main__":
    main()
