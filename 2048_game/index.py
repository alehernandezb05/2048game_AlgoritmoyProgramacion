from game import *
op = 0
while(op != 3):
    menu()
    op = int(input("Ingrese una opcion: "))
    if(op == 1):
        nombre = nombre_jugador()
        game = crear_matriz()
        vacios = espacios_vacios(game)
        game = rellenar_espacio_vacio(game, vacios)
        movimientos = 0
        num = 1
        salir = True
        
        while salir:
            os.system("cls")
            bienvenido(nombre)
            if num != 0:
                vacios = espacios_vacios(game)
                game = rellenar_espacio_vacio(game, vacios)
            
            jugada = ""
            while jugada not in ["w", "a", "s", "d", "p"]:
                os.system("cls")
                bienvenido(nombre)
                mostrar_matriz(game)
                print(f"Movimientos: {movimientos}, Puntos: {sumar_matriz(game)}")
                jugada = input("Ingrese una jugada (w/a/s/d) o presione (p) para salir: ")
                
            else:
                if jugada == "w" or jugada == "W":
                    game = mover_arriba(game)
                    movimientos += 1
                elif jugada == "a" or jugada == "A":
                    game = mover_izquierda(game)
                    movimientos += 1
                elif jugada == "s" or jugada == "S":
                    game = mover_abajo(game)
                    movimientos += 1
                elif jugada == "d" or jugada == "D":
                    game = mover_derecha(game)
                    movimientos += 1
                elif jugada == "p" or jugada == "P":
                    salir = input("¿Seguro que quieres salir? (s/n): ")
                    if salir.lower() == "s":
                        print("Gracias por jugar!")
                        salir = False
                        guardar_resultados(nombre, game, movimientos,sumar_matriz(game))
                        break
                    else:
                        continue
            
            if ganador(game):
                os.system("cls")
                mostrar_matriz(game)
                print(f"Felicidades {nombre}, has ganado!")
                guardar_resultados(nombre, game, movimientos,sumar_matriz(game))
                break
            
            if len(espacios_vacios(game)) == 0 and sin_movimientos(game) == True:
                os.system("cls")
                mostrar_matriz(game)
                print(f"{nombre}, Has perdido!")
                guardar_resultados(nombre, game, movimientos,sumar_matriz(game))
                break
    elif(op == 2):
        leer_resultados()
    elif(op == 3):
        print("Salir, Gracias por Jugar :)")
        break
    else:
        print("Opcion Invalida")
        continue