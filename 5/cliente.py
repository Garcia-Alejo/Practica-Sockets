import socket
import threading

host= "localhost"
port= 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))

nombreUser = input ("ingrese su nombre de usuario: ")
clienteSocket.send(nombreUser.encode())
print(f"Cliente {nombreUser} conectado ")

def recibirMensaje ():
	while True:
		try:
			msj= clienteSocket.recv(1024).decode()
			if msj:
				print (msj)

		except:
			print ("Conexion cerrada")
			clienteSocket.close()
			break

threading.Thread(target=recibirMensaje, daemon=True).start()

print (f"{nombreUser}")
while True:
	msj= input(f"[{nombreUser}]: ")
	if msj.lower() == "q":
		clienteSocket.send(msj.encode())
		print(f"El cliente {nombreUser} se desconecto" )
		clienteSocket.close()
		break
	clienteSocket.send(msj.encode())
