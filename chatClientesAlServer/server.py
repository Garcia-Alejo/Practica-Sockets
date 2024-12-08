import socket
import threading

def manejadorCliente(conn, addr):
	print (f"Cliente Conectado")
	while True:
		try:
			msj = conn.recv(1024).decode()
			if not msj or msj.lower() == "q":
				print (f"el Cliente {addr} se desconecto")

				break
			print(f" {addr} Mensaje: {msj}")
			conn.send("Mensaje Recibido".encode())

		except errorEnConexion:
			print(f"Existio un error en la conexion del cliente {addr}")
			break
	conn.close()

host= "localhost"
port= 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host, port))
serverSocket.listen(5)
print("server esperando conexiones...")

while True:
	conn, addr = serverSocket.accept()
	threading.Thread(target=manejadorCliente, args=(conn, addr)).start()