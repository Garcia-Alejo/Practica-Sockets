import socket

host = "localhost"
port = 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))
print("Conectado al servidor")

while True:
    palabra = input("Ingrese una palabra: ")
    clienteSocket.send(palabra.encode())

    respuesta = clienteSocket.recv(1024).decode()
    print(respuesta)

    mensajeConfirmacion = clienteSocket.recv(1024).decode()
    print(mensajeConfirmacion)

    palidromoOno = clienteSocket.recv(1024).decode()
    print(palidromoOno)

    opc = input("Si desea salir presione 'q': ")
    clienteSocket.send(opc.encode())

    if opc.lower() == "q":
        print("El cliente se desconecta")
        break

clienteSocket.close()
