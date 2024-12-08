import socket
HOST="localhost"
PORT=5050
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
conexion, direccion = server.accept()
while True:
        modificacion=conexion.recv(1024).decode()
        print(f"{modificacion}")
        mensajeC=conexion.recv(1024).decode()
        print(f"{mensajeC}")
        if modificacion=="mayus":
                mM=mensajeC.upper()
                print(f"{mM}")
                conexion.sendall(mM.encode())
        if modificacion=="minus":
                mMin=mensajeC.lower()
                print(f"{mMin}")
                conexion.sendall(mMin.encode())
        if modificacion=="reverse":
                mR=mensajeC[::-1]
                print(f"{mR}")
                conexion.sendall(mR.encode())
        else:
                error_msg = "Comando no reconocido. Intenta nuevamente."
                print(error_msg)
                conexion.sendall(error_msg.encode())
        if mensajeC=="salir":
                break
