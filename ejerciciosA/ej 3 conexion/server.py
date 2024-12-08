import socket

HOST= "localhost"
PORT= 5050

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
conexion,direccion=server.accept()
print(f"Servidor escuchando en {HOST}:{PORT}")
while True:
	mensaje=conexion.recv(1024).decode()
	print(f"el mensaje enviado fue {mensaje}")
	conexion.sendall(f"pijita".encode())

