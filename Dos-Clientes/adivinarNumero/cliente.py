import socket

port = 12345
host = "localhost"

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))
print("Conectado al servidor")

while True:
    numero = int(input("Ingresa tu número para adivinar (1 al 30): "))
    clienteSocket.send(str(numero).encode())

    respuesta = clienteSocket.recv(1024).decode()
    print("Servidor:", respuesta)

    if "¡Adivinaste el número!" in respuesta:
        break

    continuar = input("¿Quieres seguir jugando? (q para salir): ")
    clienteSocket.send(continuar.encode())

    if continuar.lower() == "q":
        break

clienteSocket.close()
print("Desconectado del servidor")
