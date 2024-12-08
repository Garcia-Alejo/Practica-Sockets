import socket

host= "localhost"
port= 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect ((host, port))

while True:

	frase = input ("ingrese su frase: ")
	clienteSocket.send(frase.encode())

	resultado = clienteSocket.recv(1024).decode()
	print(resultado)
	
