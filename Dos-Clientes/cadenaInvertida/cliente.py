import socket

port= 12345
host = "localhost"

clienteSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect ((host, port))
print ("Conexion establecida con el server")

nombreUser = input ("Bienvenido, ingrese su nombre: ")
clienteSocket.send (nombreUser.encode())

while True:

	palabra = input (f"Usuario {nombreUser} ingrese su palabra: ")
	clienteSocket.send(palabra.encode())

	respuesta = clienteSocket.recv(1024).decode()
	print (respuesta)

	palabraConcatenada= clienteSocket.recv(1024).decode()
	print(palabraConcatenada)

	opc = input("presione 'q' se quiere salir: ")
	clienteSocket.send(opc.encode())

	if opc.lower() == "q":
		print("Te desconecta")
		break

clienteSocket.close()