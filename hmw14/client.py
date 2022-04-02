import socket


class Client:
    def __init__(self):
        self.SRV_HOST = "127.0.0.1"
        self.SRV_PORT = 6969
        self.username = input("Please, enter your username: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.SRV_HOST, self.SRV_PORT))
        self.kw_refresh = ("r", "refresh")
        self.kw_quit = (r"\q", r"\quit", r"\exit")

    def close_connection(self):
        self.send_message(f"{self.username} has left the chat")
        self.client.close()

    def send_message(self, msg):
        self.client.send(f"{self.username}: {msg}".encode())

    def receive_message(self):
        print(self.client.recv(2048).decode())

    def start(self):
        self.client.send(f"'{self.username}' joined the chat".encode())
        while True:
            message = input(f"{self.username}: ")
            if message in self.kw_refresh:
                self.receive_message()
            elif message in self.kw_quit:
                self.close_connection()
                break
            else:
                self.send_message(message)


if __name__ == '__main__':
    cl1 = Client()
    cl1.start()
