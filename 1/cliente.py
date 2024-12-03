import socket

host= "localhost"
port= 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clienteSocket.connect((host, port))
print ("cenectado al servidor")

msj= "HOLA PUTO"
clienteSocket.send(msj.encode())

clienteSocket.close()