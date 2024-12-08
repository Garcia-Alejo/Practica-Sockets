import socket

host= "localhost"
port= 12345

serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host, port))
serverSocket.listen(2)
print ("El server esta escuhando conexiones...")

conn, addr = serverSocket.accept()
print(f"Se conecto al servidor: {addr}")

while True:
	frase = conn.recv(1024).decode()
	print (f"la frase que se envio fue: {frase}")

	buscarPalabra = conn.recv(1024).decode() 
	print (f"la palabra que se buscar es: {buscarPalabra}")

	#Eliminar los espacios sobrantes de una frase
	sinEspacios= " ".join(frase.split())
	print (f"la frase sin espacios adicionales es: {sinEspacios}")
	conn.send(f"la frase sin espacios adicionales es: {sinEspacios}".encode())

	#Contar las palabras de una frase
	palabras = frase.split()
	print(f"la frase contiene {len(palabras)} palabras")
	conn.send(f"la frase contiene {len(palabras)} palabras".encode())

	#Buscar cierta palabra en una frase
	if buscarPalabra.lower() in frase.lower():
		print (f"la palabra '{buscarPalabra}' se encuentra dentro de la frase")
		conn.send("la pabra que pediste esta dentro de la frase".encode())

	else:
		print (f"la palabra '{buscarPalabra}' no se encuentra dentro de la frase")
		conn.send("la pabra que pediste NO esta dentro de la frase".encode())


	conn.send("Desea continuar? presione 'q' para salir".encode())

	opc = conn.recv(1024).decode()
	if opc.lower()== "q":
		print ("el cliente se desconecta")
		break

conn.close()
serverSocket.close()
