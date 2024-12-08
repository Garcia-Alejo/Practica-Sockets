import socket
import threading
import random

port = 12345
host = "localhost"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("El servidor está escuchando conexiones...")

clientes = []
numeroRandom = random.randint(1, 30)
print(f"El número aleatorio generado por el servidor es: {numeroRandom}")

def manejadorCliente(conn, cliente_id):
    global numeroRandom

    while True:
        try:
            num = int(conn.recv(1024).decode())
            print(f"El número del cliente {cliente_id} es: {num}")

            if num > numeroRandom:
                mensaje = "El número que enviaste es mayor que el número del servidor"
            elif num < numeroRandom:
                mensaje = "El número que enviaste es menor que el número del servidor"
            else:
                mensaje = "¡Adivinaste el número! Felicidades."
                conn.send(mensaje.encode())
                break

            conn.send(mensaje.encode())

            opc = conn.recv(1024).decode()
            if opc.lower() == "q":
                print(f"El cliente {cliente_id} se ha desconectado")
                break
        except:
            print(f"Error con el cliente {cliente_id}. Cerrando conexión.")
            break

    conn.close()
    print(f"Conexión cerrada con el cliente {cliente_id}")

# Aceptar conexiones de dos clientes
for i in range(2):
    conn, addr = serverSocket.accept()
    print(f"Cliente {i+1} conectado desde: {addr}")
    clientes.append(conn)
    threading.Thread(target=manejadorCliente, args=(conn, i+1)).start()
