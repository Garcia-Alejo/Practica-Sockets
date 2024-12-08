import socket
import threading

port = 12345
host= "localhost"

serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(5)
print ("El servidor escuhando conexiones...")

clientes = []

def manejadorCliente(conn, addr):
	nombreUser = conn.recv(1024).decode()
	print (f"El cliente {nombreUser} se ha conectado")
	conn.send("Bienvenido al chat, pulsa q para salir. ".encode())

	while True:
		try:
			msj = conn.recv(1024).decode()
			if msj.lower() == "q":
				print (f"el Cliente {nombreUser} se desconecto")
				clientes.remove (conn)
				conn.close()
				break
			difundirMensaje(f"{nombreUser}: {msj}", conn)
		except:
			print("Hubo un error en la conexion")
			clientes.remove (conn)
			conn.close()
			break


def difundirMensaje(msj, remitente):
	for cliente in clientes:
		if cliente != remitente:
			try:
				cliente.send(msj.encode())
			except:
				clientes.remove()
				conn.close()


def aceptarConexiones():
	while True:
		conn, addr = serverSocket.accept()
		clientes.append(conn)
		hilo = threading.Thread(target=manejadorCliente, args=(conn, addr))
		hilo.start()

aceptarConexiones()