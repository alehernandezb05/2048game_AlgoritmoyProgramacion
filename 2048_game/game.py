import random
import os
import copy
import datetime

def menu():
    print("\t --- |- 2048 -| ---")
    print("1. Jugar")
    print("2. Leer Resultados")
    print("3. Salir")

def nombre_jugador():
    nom = input("Ingrese su Nombre: ") 

    return nom

def bienvenido(nom_jugador):
    print(f"Bienvenido al Juego 2048, {nom_jugador}!")

def crear_matriz():
    game = []
    for i in range(0,4):
        game.append([0]*4)
    return game

def mostrar_matriz(game):
    tablero = copy.deepcopy(game)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                tablero[i][j] = " "
    
    print("-" * ((7 * len(tablero) + 1)))
    for i in range(len(tablero)):
        print("|", end="")
        for j in range(len(tablero[i])):
            print(f" {tablero[i][j]:^4} |", end="")
        print("\n" + "-" * ((7 * len(tablero) + 1)))

def espacios_vacios(game):
    vacios = []
    
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == 0:
                vacios.append((i, j))
    return vacios

def rellenar_espacio_vacio(game, vacios):
    n = 2
    
    casillas = random.choice(vacios)
    game[casillas[0]][casillas[1]] = n
    return game

def mover_arriba(game):
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                for k in range(i+1, 4):
                    if game[k][j] != 0:
                        game[i][j] = game[k][j]
                        game[k][j] = 0
                        break
    for i in range(3):
        for j in range(4):
            if game[i][j] == game[i+1][j]:
                game[i][j] *= 2
                game[i+1][j] = 0
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                for k in range(i+1, 4):
                    if game[k][j] != 0:
                        game[i][j] = game[k][j]
                        game[k][j] = 0
                        break
    return game

def mover_abajo(game):
    for i in range(3, -1, -1):
        for j in range(4):
            if game[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if game[k][j] != 0:
                        game[i][j] = game[k][j]
                        game[k][j] = 0
                        break
    for i in range(3, 0, -1):
        for j in range(4):
            if game[i][j] == game[i-1][j]:
                game[i][j] *= 2
                game[i-1][j] = 0
    for i in range(3, -1, -1):
        for j in range(4):
            if game[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if game[k][j] != 0:
                        game[i][j] = game[k][j]
                        game[k][j] = 0
                        break
    return game

def mover_izquierda(game):
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                for k in range(j+1, 4):
                    if game[i][k] != 0:
                        game[i][j] = game[i][k]
                        game[i][k] = 0
                        break
    for i in range(4):
        for j in range(3):
            if game[i][j] == game[i][j+1]:
                game[i][j] *= 2
                game[i][j+1] = 0
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                for k in range(j+1, 4):
                    if game[i][k] != 0:
                        game[i][j] = game[i][k]
                        game[i][k] = 0
                        break
    return game

def mover_derecha(game):
    for i in range(4):
        for j in range(3, -1, -1):
            if game[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if game[i][k] != 0:
                        game[i][j] = game[i][k]
                        game[i][k] = 0
                        break
    for i in range(4):
        for j in range(3, 0, -1):
            if game[i][j] == game[i][j-1]:
                game[i][j] *= 2
                game[i][j-1] = 0
    for i in range(4):
        for j in range(3, -1, -1):
            if game[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if game[i][k] != 0:
                        game[i][j] = game[i][k]
                        game[i][k] = 0
                        break
    return game

def ganador(game):
    for i in range(4):
        for j in range(4):
            if game[i][j] == 2048:
                return True
    return False

def sin_movimientos(game):
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                return False
    for i in range(3):
        for j in range(3):
            if game[i][j] == game[i+1][j] or game[i][j] == game[i][j+1]:
                return False
    for i in range(3):
        if game[i][3] == game[i+1][3]:
            return False
    for j in range(3):
        if game[3][j] == game[3][j+1]:
            return False
    return True

def guardar_resultados(nombre_jugador, tablero, movimientos,punt):
    with open("resultados.txt", "a") as f:
        f.write(f"Nombre: {nombre_jugador}\n")
        f.write(f"Fecha: {datetime.datetime.now()}\n")
        f.write("Estado final del tablero:\n")
        for fila in tablero:
            f.write("\t".join(str(num) for num in fila) + "\n")
        f.write(f"Movimientos: {movimientos}, Puntos:{punt}\n\n")

def leer_resultados():
    try:
        with open("resultados.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No hay resultados guardados.")

def sumar_matriz(game):
    suma = 0
    for i in range(4):
        for j in range(4):
            suma += game[i][j]
    return suma