import socket

port= 12345
host= "localhost"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host, port))
serverSocket.listen(1)
print (f"El server esta escuchando conexiones")

conn, addr= serverSocket.accept()
print (f"Conexion estableciada con {addr}")

msj = conn.recv(1024).decode()
print(f"el mensaje recibido fue: {msj}")

conn.close()
serverSocket.close()
