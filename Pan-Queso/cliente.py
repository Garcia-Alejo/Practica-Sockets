import socket

# Configuración del cliente
port = 12345
host = "localhost"

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))

# Recibir mensaje de bienvenida
print(clienteSocket.recv(1024).decode())

# Enviar tamaño del pie
tamañoPie = input("Ingrese su tamaño de pie: ")
clienteSocket.send(tamañoPie.encode())

# Ciclo del juego
while True:
    mensaje = clienteSocket.recv(1024).decode()
    print(mensaje)

    if "¡Ganaste!" in mensaje:
        break

    if "Pulsa 'A'" in mensaje:
        accion = input("Tu acción: ")
        clienteSocket.send(accion.encode())

clienteSocket.close()
