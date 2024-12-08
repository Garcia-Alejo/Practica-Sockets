import socket
import threading

PORT = 5050
HOST = "localhost"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print(f"Servidor escuchando en {HOST}:{PORT}")

colores = []  # Lista para almacenar los colores de los jugadores


def juego(conexion, direccion, num_cliente):
    global colores
    # Solicitar color al jugador
    conexion.sendall(f"Eres el jugador {num_cliente}. Envía tu color favorito:".encode())
    colorFav = conexion.recv(1024).decode()
    print(f"Jugador {num_cliente} ({direccion}) eligió el color: {colorFav}")

    # Agregar el color del jugador a la lista
    colores.append(colorFav)
    # Esperar a que ambos jugadores envíen sus colores
    while len(colores) < 2:
        pass

    # Determinar el color del rival
    color_rival = colores[1 - num_cliente]

    conexion.sendall("Intenta adivinar el color favorito de tu rival.".encode())

    while True:
        adivinanza = conexion.recv(1024).decode()
       	print(f"{adivinanza}")
        if adivinanza in color_rival:
            print(f"El jugador {num_cliente} adivinó correctamente el color del rival!")
            conexion.sendall("¡Has adivinado correctamente!".encode())
            break  # Salir del bucle
        else:
            conexion.sendall("adivina de nuevo, no es un color flaqui.".encode())

    conexion.close()


def manejar_conexiones():
    server.listen(2)
    print("Esperando conexiones...")
    num_cliente = 0

    while num_cliente < 2:  # Limitar a dos jugadores
        conexion, direccion = server.accept()
        print(f"Jugador {num_cliente} conectado desde {direccion}")
	        hilo = threading.Thread(target=juego, args=(conexion, direccion, num_cliente))
	        hilo.start()
	        num_cliente += 1

    print("Juego iniciado con dos jugadores.")


manejar_conexiones()


