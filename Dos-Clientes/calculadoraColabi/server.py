import socket

# Configuración del servidor
host = "localhost"
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("El servidor está escuchando conexiones...")

clientes = []

# Esperar a que ambos clientes se conecten
while len(clientes) < 2:
    conn, addr = serverSocket.accept()
    print(f"Cliente conectado desde {addr}")
    clientes.append(conn)

print("Ambos clientes conectados. Esperando números...")

# Recibir un número de cada cliente
numeros = []
for i, cliente in enumerate(clientes):
    cliente.send(f"Cliente {i + 1}, envía tu número: ".encode())  # Solicitar número
    num = int(cliente.recv(1024).decode())  # Recibir número
    print(f"Número recibido del cliente {i + 1}: {num}")
    numeros.append(num)

# Realizar las operaciones
num1, num2 = numeros
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre 0"


print (f"Suma: {suma}\n")
print (f"Resta: {resta}\n")
print (f"Multiplicación: {multiplicacion}\n")
print (f"División: {division}\n")

# Cerrar conexiones
for cliente in clientes:
    cliente.close()
print("Conexiones cerradas.")
