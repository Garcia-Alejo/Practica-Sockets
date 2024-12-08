import socket
HOST="localhost"
PORT=5050
cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((HOST,PORT))
while True:
    comando=input(f"inserta el comando: minus,mayus,reverse: ")
    cliente.sendall(comando.encode())
    mensaje=input(f"que mensaje desea mandar")
    cliente.sendall(mensaje.encode())

    terminado=cliente.recv(1024).decode()
    print(f"{terminado}")
    if mensaje=="salir":
        break
