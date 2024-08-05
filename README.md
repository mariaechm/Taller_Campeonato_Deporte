# Taller_Campeonato_Deporte

# Descripcion
Permite gestionar un campeonato de Futbol en cual permite registrar equipos, jugadores asi tambien muestra sus estadisticas y realiza inscripciones a campeonatos. Esta actividad se encuentra en un diagrama de clases UML e implementado en codigo en el lenguajae de programacion Python.
  # Diagrama de Clases
  ![CampeonatoDeFutbol](https://github.com/user-attachments/assets/81a4efbb-8f69-4eb1-9f03-fc45c0714933)

  # Clases 
   * Arbitro
     Atributos:
     - id_arbitro: int (privado) -> Identificador del árbitro.
     - nombre_completo: String (privado) -> Nombre completo del árbitro.
     - nacionalidad: String (privado) -> Nacionalidad del árbitro.
    Métodos:
     + obtenerInformacion(): String (público) -> Devuelve un string (cadena de caracteres) con la informacion registrada del árbitro.
       
   * Calendario
     Atributos:
     - partidos: List<Partido> (privado) -> Lista de partidos programados.
     Métodos:
     + agregarPartido(partido: Partido) (público) -> Añade un partido a la lista.
     + partidosPorFecha(fecha: Date): List<Partido> (público) -> Devuelve una lista de partidos para una fecha determinada.
     + obtenerInformacion(): String (público) -> Devuelve un string con la informacion de calendario.
       
  * Campeonato
    Atributos:
    - id_campeonato: int (privado) -> Identificador del campeonato.
    - nombre: String (privado) -> Nombre del campeonato.
    - fecha_inicio: Date (privado) -> Fecha de inicio del campeonato.
    - fecha_fin: Date (privado) -> Fecha de finalización del campeonato.
    - tipo: String (privado) -> Tipo de campeonato (liga).
    - equipos: List<Equipo> (privado) ->Lista de equipos participantes.
    - partidos: List<Partido> (privado) -> Lista de partidos programados.
    Métodos:
   + agregarEquipo(equipo: Equipo) (público) -> Añade un equipo a la lista de equipos participantes.
   + organizarPartido(partido: Partido) (público) -> Organiza un partido y lo agrega a la lista de partidos.
   + estadisticasEquipos() (público) -> Devuelve estadísticas de los equipos.
   + estadisticasIndividuales() (público) -> Devuelve estadísticas individuales de los jugadores.
   + obtenerCampeon(): String (público) -> Devuelve el nombre del equipo campeón.
     
 * Equipo
   Atributos:
   - id_equipo: int (privado) -> Identificador del equipo.
   - nombre: String (privado) -> Nombre del equipo.
   - jugadores: List<Jugador> (privado) -> Lista de jugadores del equipo.
   - goles: int (privado) ->Total de goles anotados por el equipo.
   - puntos: int (privado) -> Puntos acumulados por el equipo.
   - goles_a_favor: int (privado) -> Goles anotados a favor del equipo.
   - goles_en_contra: int (privado) -> Goles recibidos en contra del equipo.
  Métodos:
   + incluirJugador(jugador: Jugador) (público) -> Añade un jugador a la lista de jugadores.
   + totalGoles(): int (público) -> Devuelve el total de goles anotados.
   + diferenciaGoles(): int (público) -> Devuelve la diferencia de goles (goles a favor - goles en contra).
     
 * Estadio
   Atributos:
   - id_estadio: int (privado) -> Identificador del estadio.
   - nombre: String (privado) -> Nombre del estadio.
   - ubicacion: String (privado) -> Ubicación del estadio.
   - capacidad: int (privado) -> Capacidad del estadio.
   Métodos:
   + obtenerInformacion(): String (público) -> Devuelve un string con la informacion del estadio.
     
 * Estadisticas
   Atributos:
   - campeonato: Campeonato (privado) -> Campeonato del que se generan las estadísticas.
   Métodos:
   + mostrarEstadisticasEquipos() (público) -> Muestra las estadísticas de los equipos.
   + mostrarEstadisticasIndividuales() (público) -> Muestra las estadísticas individuales de cada uno de los jugadores ingresados.
     
 * Inscripcion
   Atributos:
   - campeonato: Campeonato (privado) -> Campeonato en el cual se inscriben los equipos.
   Métodos:
   + inscribirEquipos() (público) -> Inscribe equipos en el campeonato.
     
 * Jugador
   Atributos:
   - id_jugador: int (privado) -> Identificador del jugador.
   - nombre_completo: String (privado) -> Nombre completo del jugador.
   - fecha_nacimiento: Date (privado) -> Fecha de nacimiento del jugador.
   - sexo: String (privado) -> Sexo del jugador (masculino/femenino).
   - numero_camiseta: int (privado) -> Número de camiseta del jugador.
   - peso: float (privado) -> Peso del jugador.
   - estatura: float (privado) -> Estatura del jugador.
   - goles: int (privado) -> Total de goles anotados por el jugador.
   Métodos:
   + calcularEdad(): int (público) -> Calcula y devuelve la edad del jugador.
   + estadisticasJugador() (público) -> Devuelve las estadísticas del jugador.
     
 * Partido
   Atributos:
   - id_partido: int (privado) -> Identificador del partido.
   - equipo_local: Equipo (privado) -> Equipo local que participa en el partido.
   - equipo_visitante: Equipo (privado) -> Equipo visitante que participa en el partido.
   - fecha: Date (privado) -> Fecha del partido.
   - estadio: Estadio (privado) -> Estadio donde se juega el partido.
   - arbitro: Arbitro (privado) -> Árbitro que dirige el partido.
   - goles_local: int (privado) -> Goles anotados por el equipo local.
   - goles_visitante: int (privado) -> Goles anotados por el equipo visitante.
   - sanciones: List<Sancion> (privado) -> Lista de sanciones registradas en el partido.
   Métodos:
   + disputarPartido(goles_local: int, goles_visitante: int, goleadores_local: List<Jugador>, goleadores_visitante: List<Jugador>)
     (público) -> Registra el resultado del partido.
   + registrarSancion(sancion: Sancion) (público) -> Registra una sanción en el partido.
   + resultadoPartido(): String (público) -> Devuelve el resultado del partido.
     
 * Sancion
   Atributos:
   - jugador: Jugador (privado) -> Jugador sancionado.
   - tipo: String (privado) -> Tipo de sanción (amarilla/roja/suspensión).
   - partido: Partido (privado) -> Partido en el que ocurrió la sanción.
   - motivo: String (privado) -> Motivo de la sanción.
   Métodos:
   + obtenerInformacion(): String (público) -> Devuelve un string con los detalles de la sanción.
     
 * Temporada
   Atributos:
   - anio: int (privado) -> Año de la temporada.
   - campeonatos: List<Campeonato> (privado) -> Lista de campeonatos en la temporada.
   Métodos:
   + incluirCampeonato(campeonato: Campeonato) (público) -> Añade un campeonato a la lista.
   + obtenerInformacion(): String (público) -> Devuelve un string de informacion de la temporada.
  
     
# Nombre:
 Maria Elizabeth Chuico Medina
