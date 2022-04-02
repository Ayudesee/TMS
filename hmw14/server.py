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


def delete_connected_client(rsock):
    for index, c in enumerate(CONNECTED_CLIENTS):
        if rsock == c:
            del CONNECTED_CLIENTS[index]


def send_message_to_clients(rsock):
    data = rsock.recv(2048).decode()
    # if client socket is closed
    if not data:
        delete_connected_client(rsock)
    else:
        print(data)
    # send message to all clients but sender
    for clientsock in CONNECTED_CLIENTS:
        if rsock != clientsock:
            clientsock.send(data.encode())


def append_client():
    client, addr = srv_sock.accept()
    client.setblocking(False)
    FOR_READ.append(client)
    CONNECTED_CLIENTS.append(client)


print("Server started")
# main loop
while True:
    R, W, ERR = select.select(FOR_READ, FOR_WRITE, FOR_READ)
    for r in R:
        if r is srv_sock:
            append_client()
        else:
            send_message_to_clients(r)
