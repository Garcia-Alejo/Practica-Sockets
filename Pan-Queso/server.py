import socket
import threading

# Configuración del servidor
port = 12345
host = "localhost"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("El servidor está escuchando conexiones...")

# Variables del juego
distanciaInicial = 10
jugadores = []
tamañoPies = {}

# Bloqueo para sincronizar el acceso a la distancia
lock = threading.Lock()

# Función para manejar cada jugador
def manejar_jugador(cliente_socket, id_jugador):
    global distanciaInicial

    # Enviar mensaje inicial
    cliente_socket.send(f"Bienvenido jugador {id_jugador + 1}. La distancia inicial es {distanciaInicial}.".encode())

    # Recibir tamaño del pie
    tamañoPie = int(cliente_socket.recv(1024).decode())
    tamañoPies[id_jugador] = tamañoPie
    print(f"Tamaño del pie del jugador {id_jugador + 1}: {tamañoPie}")

    while True:
        # Enviar mensaje al jugador con la distancia actual
        cliente_socket.send(f"Distancia restante: {distanciaInicial}. Pulsa 'A' para avanzar.".encode())
        accion = cliente_socket.recv(1024).decode()

        if accion.lower() == "a":
            with lock:
                # Restar el tamaño del pie a la distancia compartida
                distanciaInicial -= tamañoPie
                print(f"Jugador {id_jugador + 1} avanzó {tamañoPie}. Distancia restante: {distanciaInicial}")

                # Verificar si alguien ganó
                if distanciaInicial <= 0:
                    cliente_socket.send("¡Ganaste! La distancia llegó a 0.".encode())
                    print(f"Jugador {id_jugador + 1} ganó la partida.")
                    for jugador in jugadores:
                        if jugador != cliente_socket:
                            jugador.send("Perdiste. La distancia llegó a 0.".encode())
                    break

        else:
            cliente_socket.send("No pulsaste 'A'. Intenta de nuevo.".encode())

    cliente_socket.close()


# Aceptar conexiones
while len(jugadores) < 2:
    cliente_socket, addr = serverSocket.accept()
    print(f"Jugador conectado desde {addr}")
    jugadores.append(cliente_socket)
    id_jugador = len(jugadores) - 1
    threading.Thread(target=manejar_jugador, args=(cliente_socket, id_jugador)).start()

serverSocket.close()
