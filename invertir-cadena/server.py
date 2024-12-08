import socket

port = 12345
host = "localhost"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("El servidor está escuchando conexiones...")

conn, addr = serverSocket.accept()
print(f"Se estableció la conexión con: {addr} ")

def invertirCadena(cadena):
    return cadena[::-1]

while True:
    palabra = conn.recv(1024).decode()
    print(f"La palabra que se envió fue: {palabra}")

    palabraInvertida = invertirCadena(palabra)
    print(f"La palabra invertida es: {palabraInvertida}")
    conn.send(f"La palabra invertida quedó: {palabraInvertida}".encode())

    if palabra.lower() == palabraInvertida.lower():
        print("La palabra es un palíndromo")
        conn.send("**La palabra es un palíndromo**".encode())
    else:
        print("La palabra no es un palíndromo")
        conn.send("**La palabra NO es un palíndromo**".encode())

    conn.send("¿Desea continuar? Presione 'q' para salir".encode())

    opc = conn.recv(1024).decode()
    if opc.lower() == "q":
        print("El cliente se desconecta")
        break

conn.close()
print("Conexión cerrada")
