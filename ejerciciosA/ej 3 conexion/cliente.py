import socket
HOST="localhost"
PORT=5050

cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((HOST,PORT))

while True:
	clienteM=input(f"escribi un mensaje para mandar ")
	cliente.sendall(clienteM.encode())
	respuesta=cliente.recv(1024).decode()
	print(f"el servidor le dice{respuesta}")



