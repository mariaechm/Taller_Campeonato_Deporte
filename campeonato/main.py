from campeonato_controller import CampeonatoController
from equipo_controller import EquipoController
from input_view import InputView
from output_view import OutputView

def main():
    campeonato_controller = CampeonatoController()
    equipo_controller = EquipoController()
    input_view = InputView()
    output_view = OutputView()

    # Obtener datos de entrada
    datos_campeonato = input_view.obtener_datos_campeonato()
    datos_equipo = input_view.obtener_datos_equipo()

    # Agregar campeonatos y equipos
    campeonato_controller.agregar_campeonato(datos_campeonato)
    equipo_controller.agregar_equipo(datos_equipo)

    # Mostrar resultados y tabla de posiciones
    output_view.mostrar_resultados(campeonato_controller)

if __name__ == "__main__":
    main()
