import socket
import select

FOR_READ = []
FOR_WRITE = []

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6969

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_sock.bind((SERVER_HOST, SERVER_PORT))
srv_sock.listen(20)

srv_sock.setblocking(False)
FOR_READ.append(srv_sock)

BUFFER = {}
CONNECTED_CLIENTS = []

print("Server started")
while True:
    R, W, ERR = select.select(FOR_READ, FOR_WRITE, FOR_READ)
    for r in R:
        if r is srv_sock:
            client, addr = srv_sock.accept()
            client.setblocking(False)
            FOR_READ.append(client)
            CONNECTED_CLIENTS.append(client)
        else:
            data = r.recv(2048).decode()
            if not data:
                for index, c in enumerate(CONNECTED_CLIENTS):
                    if r == c:
                        del CONNECTED_CLIENTS[index]
            else:
                print(data)
            for c in CONNECTED_CLIENTS:
                if r != c:
                    c.send(data.encode())
