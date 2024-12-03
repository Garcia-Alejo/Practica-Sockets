import socket

host = "localhost"
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)

print ("servidor escuchando conexiones....")

conn, addr= serverSocket.accept()
print (f"Conexion estableciada con {addr}")

frase = conn.recv(1024).decode()
print(f"la frase enviada fue: {frase}")

vocales = "aeiouAEIOU"
vocalesEncontradas = []
contador = 0

for letra in frase:
	if letra in vocales:
		contador+=1
		vocalesEncontradas.append(letra)

print (f"la frase contiene {contador} vocales. y las vocales fueron: {vocalesEncontradas}")

conn.send(f"tu frase contiene {contador} vocales y las vocales fueron: {vocalesEncontradas}".encode())
