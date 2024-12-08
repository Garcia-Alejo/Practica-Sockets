import socket
import threading

HOST = "localhost"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print(f"Servidor escuchando en {HOST}:{PORT}")

jugadores = []
numeros_a_adivinar = [None, None]  # Para almacenar los números proporcionados por los jugadores

# Manejar a cada jugador
def manejar_jugador(conexion, id_jugador):
    global jugadores, numeros_a_adivinar

    # Recibir el número que este jugador desea que el otro adivine
    numero_a_adivinar = int(conexion.recv(1024).decode())
    print(f"Jugador {id_jugador + 1} eligió el número {numero_a_adivinar}")
    numeros_a_adivinar[id_jugador] = numero_a_adivinar

    # Esperar hasta que ambos números estén disponibles
    while None in numeros_a_adivinar:
        pass

    # Informar al jugador que puede comenzar
    conexion.sendall("¡Comienza el juego!".encode())

    # El número que este jugador debe adivinar es el del oponente
    numero_del_oponente = numeros_a_adivinar[1 - id_jugador]

    while True:
        adivinanza = int(conexion.recv(1024).decode())

        if adivinanza == numero_del_oponente:
            conexion.sendall("ganaste".encode())
            print(f"Jugador {id_jugador + 1} adivinó correctamente.")
            break
        elif adivinanza > numero_del_oponente:
            conexion.sendall("El número es menor. Intenta de nuevo.".encode())
        else:
            conexion.sendall("El número es mayor. Intenta de nuevo.".encode())

    conexion.close()

# Controlar la conexión con los jugadores
def controlar_juego():
    global jugadores
    server.listen(2)
    print("Esperando jugadores...")

    while len(jugadores) < 2:
        conexion, direccion = server.accept()
        print(f"Jugador conectado desde {direccion}")
        jugadores.append(conexion)
        id_jugador = len(jugadores) - 1  # ID del jugador (0 o 1)
        hilo = threading.Thread(target=manejar_jugador, args=(conexion, id_jugador))
        hilo.start()

controlar_juego()
