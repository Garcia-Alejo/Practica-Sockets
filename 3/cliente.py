import socket

host= "localhost"
port= 12345

clieteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clieteSocket.connect((host, port))
print ("Cliente conecetado!!")

while True:
	msj= input ("Cliente: ")
	clieteSocket.send(msj.encode())

	if msj.lower() == "q":
		print ("El Cliente se desconecta")
		break

	rta = clieteSocket.recv(1024).decode()
	if rta.lower() == "1":
		print("El server cerro la conexion")
		break
	print(f"servidor: {rta} ")

clieteSocket.close()
