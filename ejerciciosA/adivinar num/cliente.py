import socket

HOST = "localhost"
PORT = 5050

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Enviar el número que este cliente desea que el oponente adivine
numero_propio = input("Elige un número para que tu oponente adivine: ")
cliente.sendall(numero_propio.encode())

# Esperar la señal de inicio del servidor
mensaje_inicio = cliente.recv(1024).decode()
print(mensaje_inicio)

# Comienza el juego
while True:
    adivinanza = input("¿Cuál crees que es el número de tu oponente?: ")
    cliente.sendall(adivinanza.encode())
    respuesta_servidor = cliente.recv(1024).decode()
    print(respuesta_servidor)

    if respuesta_servidor == "ganaste":
        print("¡Felicidades! Has ganado.")
        break

