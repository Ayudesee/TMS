import socket
import select


class Server:
    def __init__(self):
        self.FOR_READ = []
        self.FOR_WRITE = []
        self.SERVER_HOST = "127.0.0.1"
        self.SERVER_PORT = 6969
        self.srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._srv_socket_settings()
        self.BUFFER = {}
        self.CONNECTED_CLIENTS = []

    def _srv_socket_settings(self):
        self.srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv_sock.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.srv_sock.listen(20)
        self.srv_sock.setblocking(False)
        self.FOR_READ.append(self.srv_sock)

    def delete_connected_client(self, rsock):
        for index, c in enumerate(self.CONNECTED_CLIENTS):
            if rsock == c:
                del self.CONNECTED_CLIENTS[index]

    def send_message_to_clients(self, rsock):
        data = rsock.recv(2048).decode()
        # if client socket is closed
        if not data:
            self.delete_connected_client(rsock)
        else:
            print(data)
        # send message to all clients but sender
        for clientsock in self.CONNECTED_CLIENTS:
            if rsock != clientsock:
                clientsock.send(data.encode())

    def append_client(self):
        client, addr = self.srv_sock.accept()
        client.setblocking(False)
        self.FOR_READ.append(client)
        self.CONNECTED_CLIENTS.append(client)

    def start(self):
        print("Server started")
        while True:
            R, W, ERR = select.select(self.FOR_READ, self.FOR_WRITE, self.FOR_READ)
            for r in R:
                if r is self.srv_sock:
                    self.append_client()
                else:
                    self.send_message_to_clients(r)


if __name__ == "__main__":
    srv = Server()
    srv.start()
