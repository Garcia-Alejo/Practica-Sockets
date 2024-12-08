import socket
import threading

host = "localhost"
port = 12345

# Lista de productos disponibles
productos = ["Manzana - $10", "Pera - $15", "Banana - $8"]

# Carrito compartido entre todos los clientes
carrito = []

# Lista de clientes conectados
clientes = []
nombres_clientes = {}

def manejarCliente(clienteSocket, addr):
    global carrito

    # Recibir el nombre del cliente
    nombreUser = clienteSocket.recv(1024).decode()
    nombres_clientes[clienteSocket] = nombreUser
    print(f"Cliente [{nombreUser}] conectado desde {addr}")

    # Enviar la lista de productos al cliente
    listaProductos = "\n".join([f"{i+1}. {producto}" for i, producto in enumerate(productos)])
    clienteSocket.send(listaProductos.encode())

    while True:
        # Recibir la opción del cliente (producto o 'q' para finalizar)
        opcionCompra = clienteSocket.recv(1024).decode()

        if opcionCompra.lower() == 'q':
            # El cliente quiere finalizar la compra
            break

        # Validar que la opción esté dentro del rango de productos
        try:
            opcion = int(opcionCompra) - 1  # Convertir a índice
            if 0 <= opcion < len(productos):
                productoSeleccionado = productos[opcion]
                carrito.append(productoSeleccionado)  # Añadir al carrito compartido
                # Confirmar al cliente que el producto fue añadido
                clienteSocket.send(f"Producto añadido: {productoSeleccionado}".encode())
            else:
                clienteSocket.send("Opción inválida. Intenta de nuevo.".encode())
        except ValueError:
            clienteSocket.send("Opción inválida. Intenta de nuevo.".encode())

        # Enviar el carrito actualizado a todos los clientes conectados
        carritoActualizado = "\n".join(carrito)
        for c in clientes:
            c.send(f"\nCarrito compartido actualizado:\n{carritoActualizado}".encode())

    # Enviar el resumen de la compra al cliente que se desconecta
    resumen = "\n".join(carrito)
    clienteSocket.send(f"Resumen de tu compra:\n{resumen}".encode())

    # Notificar a todos los clientes sobre la desconexión
    clienteSocket.close()
    print(f"Cliente [{nombres_clientes[clienteSocket]}] desconectado.")

    # Enviar el resumen a los demás clientes
    for c in clientes:
        if c != clienteSocket:
            c.send(f"\nEl cliente [{nombres_clientes[clienteSocket]}] se ha desconectado. Su resumen de compra fue:\n{resumen}".encode())

    # Eliminar el cliente de la lista
    clientes.remove(clienteSocket)
    del nombres_clientes[clienteSocket]

def aceptarClientes():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(2)
    print("El servidor está escuchando conexiones...")

    while len(clientes) < 2:
        clienteSocket, addr = serverSocket.accept()
        print(f"Cliente conectado desde {addr}")
        clientes.append(clienteSocket)

        # Crear un hilo para manejar al cliente
        hilo = threading.Thread(target=manejarCliente, args=(clienteSocket, addr))
        hilo.start()

    serverSocket.close()

aceptarClientes()

