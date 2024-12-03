import socket
import threading

host = "localhost"
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("El servidor está escuchando conexiones...")

listaOpciones = ["1- Dibu", "2- Van Dijk", "3- Modric", "4- Martínez", "5- Messi"]

def manejadorCliente(conn):
    try:
        opciones = "\n".join(listaOpciones)
        conn.send(f"Elija una opción:\n{opciones}\n".encode())
        opcion = conn.recv(1024).decode().strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(listaOpciones):
            seleccion = listaOpciones[int(opcion) - 1]
            print(f"El cliente eligió: {seleccion}")
        else:
            print("El cliente eligió una opción inválida.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def aceptarClientes():
    while True:
        conn, _ = serverSocket.accept()
        print("Conexión establecida.")
        hilo = threading.Thread(target=manejadorCliente, args=(conn,))
        hilo.start()

aceptarClientes()
