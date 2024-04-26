jugadas = {"piedra": "tijera","papel": "piedra","tijera": "papel"}

jugador1Puntaje = 0
jugador2Puntaje = 0

while True:
    jugador1 = input("Jugador 1 ¿Piedra, papel o tijera?: ")
    jugador2 = input("Jugador 2 ¿Piedra, papel o tijera?: ")

    while jugador1 not in {"piedra": "tijera","papel": "piedra","tijera": "papel"}:
        print("No valido. Por favor ingrese: piedra, papel o tijera")
        jugador1 = input("Jugador 1 ¿Piedra, papel o tijera?: ")
        
    while jugador2 not in {"piedra": "tijera","papel": "piedra","tijera": "papel"}:
        print("No valido. Por favor ingrese: piedra, papel o tijera")
        jugador2 = input("Jugador 2 ¿Piedra, papel o tijera?: ")

    if jugadas[jugador1] == jugador2:
        jugador1Puntaje += 1
        ganador = "Jugador 1"
    elif jugadas[jugador2] == jugador1:
        jugador2Puntaje += 1
        ganador = "Jugador 2"

    print(f"Jugador 1 = {jugador1Puntaje}, Jugador 2 = {jugador2Puntaje}")

    if jugador1Puntaje == 3:
        print("¡El ganador es el Jugador 1!")
        break
    elif jugador2Puntaje == 3:
        print("¡El ganador es el Jugador 2!")
        break