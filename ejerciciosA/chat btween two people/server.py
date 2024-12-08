import socket
import threading

HOST = "localhost"
PORT = 5050
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
clientes = {}  # Diccionario para relacionar sockets con nombres


def manejar_cliente(conexion, direccion):
    """
    Función para manejar la comunicación con cada cliente.
    """
    global clientes
 
    nombre_cliente = conexion.recv(1024).decode()
    clientes[conexion] = nombre_cliente
    print(f"El cliente {nombre_cliente} se ha conectado desde {direccion}.")
        
        # Enviar mensaje de bienvenida
    conexion.sendall("Te has conectado al chat. Escribe para comunicarte.".encode())
        
        # Bucle para recibir y retransmitir mensajes
    while True:
        mensaje = conexion.recv(1024).decode()
        if mensaje.lower() == "q":  # Cliente quiere desconectarse
            print(f"{nombre_cliente} se ha desconectado.")
            break
            
            # Reenviar mensaje a otros clientes
        mensaje_formateado = f"{nombre_cliente}: {mensaje}"
        for cliente in clientes:
            if cliente != conexion:
                cliente.sendall(mensaje_formateado.encode())


def arrancar_servidor():
    """
    Función para iniciar el servidor y aceptar conexiones.
    """
    server.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}...")
    while True:
        conexion, direccion = server.accept()
        # Crear hilo para manejar al cliente
        hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
        hilo.start()


arrancar_servidor()

