j1 = 'X'
j2 = 'O'
nj = '+'

def bienvenida():
    print("Binvenidos al mejor triqui de consola que hay")
    print("Este juego esta pensado para 2 jugadores asi", end=' ') 
    print("que no seas mala leche y busca un amigo para jugar")

def triqui(tablero:"matriz") -> bool:
    if tablero[0][0] != nj and tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return True
    elif tablero[0][2] != nj and tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return True
    elif tablero[0][0] != nj and tablero[0][0] == tablero[1][0] == tablero[2][0]:
        return True
    elif tablero[0][1] != nj and tablero[0][1] == tablero[1][1] == tablero[2][1]:
        return True
    elif tablero[0][2] != nj and tablero[0][2] == tablero[1][2] == tablero[2][2]:
        return True
    elif tablero[0][0] != nj and tablero[0][0] == tablero[0][1] == tablero[0][2]:
        return True
    elif tablero[1][0] != nj and tablero[1][0] == tablero[1][1] == tablero[1][2]:
        return True
    elif tablero[2][0] != nj and tablero[2][0] == tablero[2][1] == tablero[2][2]:
        return True
    else:
        return False

def tablero_lleno(tablero:"matriz") -> bool:
    for fila in tablero:
        for elemento in fila:
            if elemento == nj:
                return False
    return True

def imprimir_tablero(tablero:"matriz"):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end='\t')
        print()

def cambiar_jugador(jugador:str) -> str:
    if jugador == j1:
        return j2
    else:
        return j1

def leer_jugada() -> (int, int):
    fila = int(input("Porfavor ingrese la fila: "))
    columna = int(input("Porfavor ingrese la columna: "))
    return fila, columna

def jugada_valida(fila:int, columna:int, tablero:"matriz") -> bool:
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == nj

def hacer_jugada(tablero:"matriz", jugador:str) -> "matriz":
    es_valida = False
    while not es_valida:
        fila, columna = leer_jugada()
        if jugada_valida(fila, columna, tablero):
            tablero[fila][columna] = jugador
            es_valida = True
        else:
            print("Esta jugada no es válida")
    return tablero


def imprimir_ganador(tablero:"matriz", jugador:str):
    imprimir_tablero(tablero)
    if triqui(tablero):
        if jugador == j1:
            print("El jugador 1 gana")
        else:
            print("El jugador 2 gana")
    else:
        print("Empate")


def main():
    bienvenida()
    jugador:str = nj
    tablero:"matriz" = [
        [nj, nj, nj],
        [nj, nj, nj],
        [nj, nj, nj]
    ]
    while not (triqui(tablero) or tablero_lleno(tablero)):
        imprimir_tablero(tablero)
        jugador = cambiar_jugador(jugador)
        tablero = hacer_jugada(tablero, jugador)
    
    imprimir_ganador(tablero, jugador)

main()