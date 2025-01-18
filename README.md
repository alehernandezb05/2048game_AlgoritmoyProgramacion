# 2048game_AlgoritmoyProgramacion
Proyecto final 2do semestre para la materia Algoritmo y Programación, UCAB. Python (py)

El juego consiste en mover las piezas en sentido arriba-abajo, abajo-arriba, izquierda-derecha, derecha-izquierda, con una teclas del teclado de la computadora. Esto ocasionará que los número de las filas (en caso de moverse verticalmente) se desplacen en la dirección indicada y si existen dos coincidentes se sumen, lo mismo en caso que se muevan horizontalmente, pero en este caso son las columnas las que se desplazan. El objetivo del juego es conseguir llegar a 2048 en alguna de las posiciones.

Cada equipo debe crear su versión de este juego usando Python y de acuerdo a los
siguientes requerimientos:
1. Inicio del Juego:
- Al iniciar el juego, solicitar el nombre del jugador
- Generar un tablero 4x4 con dos números 2 colocados aleatoriamente.
-  Mostrar el tablero en la terminal.
  
2. Movimientos y Juego:
- Permitir movimientos utilizando las teclas W, A, S, D para arriba, izquierda, abajo y derecha respectivamente.
- Cada vez que se realiza un movimiento, agregar un nuevo número 2 en una posición aleatoria del tablero.
- Si se combinan dos números iguales en un movimiento, sumarlos y duplicar el resultado.

3. Finalización del Juego:
- Finaliza la partida cuando no haya más opciones de generar un número 2, ya que todas las casillas están ocupadas, o bien, cuando el jugador decida abandonar.
- Permitir al jugador presionar la tecla P en cualquier momento para abandonar la partida. Mostrar un mensaje de confirmación antes de salir para evitar salidas accidentales.
- Cualquiera sea la forma de finalización se debe guardar en un archivo de texto:
◦ Nombre del jugador.
◦ Fecha y hora de la partida.
◦ Estado final del tablero.
◦ Cantidad de movimientos
◦ Cantidad de puntos generados

5. Leer y Mostrar Resultados:
- Implementar una opción para leer el archivo de resultados.
- Mostrar la información guardada en el archivo, incluyendo el nombre del jugador, fecha de la partida y el estado final del tablero.
  
Un ejemplo de la pantalla en la terminal sería este:
Bienvenido al Juego 2048, [Nombre del Jugador]!
-----------------------------
| 2 | 4 | 8 | 2 |
-----------------------------
| | | 2 | 32 |
-----------------------------
| | | | 2 |
-----------------------------
| | | | |
-----------------------------
Utiliza las teclas W, A, S, D para moverte. Presiona P para salir.

El archivo de salida debe mostrar las diferentes partidas jugadas y guardadas en él, además
mostrando el nombre del jugador y la fecha, hora de finalización de la partida y una impresión
de cómo quedó la pantalla al finalizar
