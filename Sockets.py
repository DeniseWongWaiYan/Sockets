import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:

        while True:
            data = connection.recv(16)
            print(data)
            if data:
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()
