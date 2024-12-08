import socket

port= 12345
host= "localhost"

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))
print ("Conectado al server")


while True:
	frase = input("Ingrese su frase: ")
	clienteSocket.send(frase.encode())

	buscarPalabra = input ("Ingrese la palabra que quiera buscar: ")
	clienteSocket.send(buscarPalabra.encode())

	sinEspacios = clienteSocket.recv(1024).decode()
	print(sinEspacios)

	palabras = clienteSocket.recv(1024).decode()
	print (palabras)

	buscarPalabra = clienteSocket.recv(1024).decode()
	print(buscarPalabra)

	opc = input ("si desea salir presione 'q':  ")
	clienteSocket.send(opc.encode())

	if opc.lower() == "q" :
		print("el cliente se desconecta")
		break


clienteSocket.close()
