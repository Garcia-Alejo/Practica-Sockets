import socket

port= 12345
host= "localhost"

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketCliente.connect((host, port))

nombreUser = input ("Ingrese nombre de usuario: ")
socketCliente.send(nombreUser.encode())
print(f"Cliente {nombreUser} conectado ")

while True:
	msj= input (f"{nombreUser}: ")
	if msj.lower() == "q":
		print ("El Cliente se desconecta")
		break
	socketCliente.send(msj.encode())


conn.close()
socketCliente.close()