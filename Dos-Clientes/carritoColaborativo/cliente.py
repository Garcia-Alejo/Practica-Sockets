import socket

host = "localhost"
port = 12345

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))

nombreUser = input("Ingrese su nombre de usuario: ")
clienteSocket.send(nombreUser.encode())
print(f"Cliente [{nombreUser}] conectado al servidor.")

# Bucle principal para seleccionar productos
while True:
    listaProductos = clienteSocket.recv(1024).decode()  # Recibe la lista de productos
    print(f"Los productos existentes son:\n{listaProductos}")  # Muestra la lista de productos

    # Pregunta al usuario qué producto desea llevar
    opcionCompra = input("¿Qué producto desea llevar? (Ingresa el número o 'q' para finalizar): ")

    if opcionCompra.lower() == 'q':
        clienteSocket.send(opcionCompra.encode())  # Enviar 'q' para finalizar
        break  # Sale del bucle si el cliente quiere finalizar

    clienteSocket.send(opcionCompra.encode())  # Enviar la opción seleccionada

    # Espera la respuesta del servidor con la confirmación de la selección
    respuesta = clienteSocket.recv(1024).decode()
    print(respuesta)  # Muestra la confirmación

    # Espera y muestra el carrito actualizado con productos de ambos clientes
    carritoActualizado = clienteSocket.recv(1024).decode()
    print(f"\nCarrito compartido:\n{carritoActualizado}")

# Recibir el resumen de la compra
resumen = clienteSocket.recv(1024).decode()
print(f"Resumen de su compra:\n{resumen}")

clienteSocket.close()
