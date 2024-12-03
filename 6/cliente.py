import socket

host = "localhost"
port = 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))
print ("El cliente se ha conectado")

try:
	bienvenida= clienteSocket.recv(1024).decode()
	print (bienvenida)

	opciones = clienteSocket.recv (1024).decode()
	print(opciones)

	opcion = input("Seleccione su eleccion de la lista").strip()
	clienteSocket.send(opcion.encode())
finally:
	clienteSocket.close()
	print ("el cliente se desconecto")
clienteSocket.close()