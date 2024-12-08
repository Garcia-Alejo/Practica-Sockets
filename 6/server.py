import socket
import threading

# Configuración del servidor
host = "localhost"
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(2)
print("Servidor escuchando conexiones...")

# Opciones disponibles
opciones = ["Rojo", "Azul", "Verde", "Amarillo"]
print(f"Opciones disponibles: {opciones}")

# Lista para almacenar las conexiones y las elecciones
clientes = []
elecciones = [None, None]  # Guardar las elecciones de los dos clientes

def manejador_cliente(conn, cliente_id):
    global elecciones
    try:
        # Enviar las opciones al cliente
        conn.send(f"Opciones disponibles: {', '.join(opciones)}".encode())
        conn.send(f"Selecciona una opción enviando el índice (0-{len(opciones)-1}): ".encode())

        # Recibir la elección del cliente
        eleccion = int(conn.recv(1024).decode())
        if 0 <= eleccion < len(opciones):
            elecciones[cliente_id] = opciones[eleccion]
            print(f"Cliente {cliente_id+1} eligió: {opciones[eleccion]}")
            conn.send(f"Elegiste: {opciones[eleccion]}".encode())
        else:
            conn.send("Índice inválido. Desconexión.".encode())
            conn.close()
            return

        # Esperar hasta que ambos clientes hayan elegido
        while None in elecciones:
            pass

        # Comparar las elecciones
        if elecciones[0] == elecciones[1]:
            mensaje = f"Ambos eligieron la misma opción: {elecciones[0]}"
        else:
            mensaje = f"Cliente 1 eligió: {elecciones[0]}, Cliente 2 eligió: {elecciones[1]}"
        
        conn.send(mensaje.encode())

    except Exception as e:
        print(f"Error con el cliente {cliente_id+1}: {e}")
    finally:
        conn.close()
        print(f"Conexión cerrada con el cliente {cliente_id+1}")

# Aceptar conexiones de dos clientes
for i in range(2):
    conn, addr = server_socket.accept()
    print(f"Cliente {i+1} conectado desde: {addr}")
    clientes.append(conn)
    threading.Thread(target=manejador_cliente, args=(conn, i)).start()

# Esperar a que todos los hilos terminen
for conn in clientes:
    conn.close()

print("Servidor cerrado.")
