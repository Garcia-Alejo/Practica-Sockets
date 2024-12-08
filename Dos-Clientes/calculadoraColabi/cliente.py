import socket

host = "localhost"
port = 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))
print("Conectado al servidor")

# Recibir mensaje del servidor
mensaje = clienteSocket.recv(1024).decode()
print(mensaje)

# Enviar número al servidor
numero = input("Ingresa tu número: ")
clienteSocket.send(numero.encode())

# Recibir resultados del servidor
resultados = clienteSocket.recv(1024).decode()
print("Resultados recibidos del servidor:")
print(resultados)

clienteSocket.close()
print("Conexión cerrada")
