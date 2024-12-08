import socket
import threading

HOST = "localhost"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

print(f"Servidor escuchando en {HOST}:{PORT}")

# Función para manejar los mensajes de cada cliente
def mensaje(conexion, direccion,num_chatters):
    conexion.sendall("Escribe cualquier mensaje:".encode())
    while True:
        mensaje = conexion.recv(1024).decode()
        print(f"Mensaje de {num_chatters}: {mensaje}")
        if mensaje == "lol":
            print("Cliente desconectado")
            break
    conexion.close()

# Función principal para controlar el chat
def control_chat():
    server.listen(2)
    print("Servidor en espera de conexiones...")
    num_chatters = 1  # Inicializar variable
    while num_chatters < 3:
        conexion, direccion = server.accept()
        print(f"Se conectó el chateador {num_chatters} en la dirección {direccion}")
        hilo = threading.Thread(target=mensaje, args=(conexion, direccion, num_chatters))
        hilo.start()
        num_chatters += 1

control_chat()

