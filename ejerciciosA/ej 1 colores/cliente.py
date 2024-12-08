import socket 
import threading

PORT=5050
HOST="localhost"
cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

color = input("¿cual es tu color favorito? ")
cliente.sendall(color.encode())

while True: 
    mensaje = cliente.recv(1024).decode()
    print(mensaje) 

    if "adivina" in mensaje:
        respuesta = input("> ")
        cliente.send(respuesta.encode())

    if "¡Has adivinado correctamente!" in mensaje:
        print("¡Felicidades, ganaste!")
        break

cliente.close()
