import socket

HOST = "localhost"
PORT = 5050

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Enviar nombre del cliente
nombre = input("Ingresa tu nombre: ")
cliente.sendall(nombre.encode())


def recibir_mensajes():
    """
    Función para recibir mensajes del servidor y mostrarlos.
    """
    while True:
        bienvenida= cliente.recv(1024).decode()
        print(f"{bienvenida}")
        mensajeC=cliente.recv(1024).decode()
        if mensajeC:
            print(f"{mensajeC}")
        else:
            break
     



# Crear hilo para recibir mensajes
import threading
hilo_recibir = threading.Thread(target=recibir_mensajes, daemon=True)
hilo_recibir.start()

# Bucle para enviar mensajes
while True:
    mensaje = input("Tú: ")
    if mensaje.lower() == "q":  # Salir del chat
        cliente.sendall("q".encode())
        break
    cliente.sendall(mensaje.encode())

