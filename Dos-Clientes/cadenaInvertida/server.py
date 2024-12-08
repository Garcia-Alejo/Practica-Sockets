import socket
import threading

host = "localhost"
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("El servidor está escuchando conexiones")

palabras_concatenadas = ""
lock = threading.Lock()


def invertirCadena(cadena):
    return cadena[::-1]

def manejadorCliente(conn, addr):
    global palabras_concatenadas

    nombreUser = conn.recv(1024).decode() 
    print(f"Cliente conectado: {nombreUser} desde {addr}")

    while True:
        palabra = conn.recv(1024).decode()
        print(f"La palabra que se recibió del cliente {nombreUser} fue {palabra}")

        palabraInvertida = invertirCadena(palabra)
        print(f"La palabra invertida del usuario {nombreUser} es: {palabraInvertida}")
        conn.send(f"La palabra invertida de {nombreUser} quedó: {palabraInvertida}".encode())

        with lock:
            palabras_concatenadas += palabra + " "
            print(f"Estado actual de palabras concatenadas: {palabras_concatenadas.strip()}")

        conn.send(f"Palabras concatenadas hasta ahora: {palabras_concatenadas.strip()}".encode())

        opc = conn.recv(1024).decode()
        if opc.lower() == "q":
            print(f"El usuario {nombreUser} se ha desconectado")
            break

    conn.close()
    print(f"Conexión cerrada con {nombreUser}")


def aceptarClientes():
    while True:
        conn, addr = serverSocket.accept()
        print("Conexión establecida con", addr)
        hilo = threading.Thread(target=manejadorCliente, args=(conn, addr))
        hilo.start()


aceptarClientes()
