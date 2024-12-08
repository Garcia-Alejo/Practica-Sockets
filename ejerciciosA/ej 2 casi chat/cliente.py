import socket
import threading

HOST="localhost"
PORT= 5050

cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((HOST,PORT))

while True: 
	tu_mensaje = input("escribi cualquier cosa, si queres salir escribi lol")
	cliente.sendall(tu_mensaje.encode())
	if tu_mensaje=="lol":
		break

cliente.close()