import socket

host= "localhost"
port= 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host, port))
serverSocket.listen(1)
print("server esperando conexiones...")

conn, addr = serverSocket.accept()
print(f"Conexion establecida {addr}")

while True:

	msj = conn.recv(1024).decode()
	if msj.lower() == "q":
		print ("el Cliente se desconecto")
		break
	print(f"Mensaje: {msj}")

	rta = input("Servidor: ")
	conn.send (rta.encode())
	
	if rta.lower() == "1":
		print("el servidor cerro la conexion")
		break

conn.close()
serverSocket.close()
