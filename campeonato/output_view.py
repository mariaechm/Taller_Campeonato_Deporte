from campeonato_controller import CampeonatoController
class OutputView:
    def mostrar_resultados(self, campeonato_controller):
        print(campeonato_controller)

    def mostrar_tabla_posiciones(self, campeonato):
        print(campeonato.tabla_posicion)
