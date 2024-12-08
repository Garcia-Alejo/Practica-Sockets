import socket

# Configuración del cliente
host = "localhost"
port = 12345

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((host, port))
print("Conectado al servidor")

try:
    # Recibir las opciones
    opciones = cliente_socket.recv(1024).decode()
    print(opciones)

    # Enviar la elección
    eleccion = input(cliente_socket.recv(1024).decode())
    cliente_socket.send(eleccion.encode())

    # Recibir la respuesta del servidor
    respuesta = cliente_socket.recv(1024).decode()
    print("Servidor:", respuesta)

finally:
    cliente_socket.close()
    print("Conexión cerrada")
