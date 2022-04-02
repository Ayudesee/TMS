import socket


SRV_HOST = "127.0.0.1"
SRV_PORT = 6969

username = input("Please, enter your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SRV_HOST, SRV_PORT))
kw_refresh = ("r", "refresh")
kw_quit = (r"\q", r"\quit", r"\exit")


def close_connection(clsock):
    send_message(clsock, f"{username} has left the chat")
    clsock.close()


def send_message(clsock, msg):
    clsock.send(f"{username}: {msg}".encode())


def receive_message(clsock):
    print(clsock.recv(2048).decode())


client.send(f"'{username}' joined the chat".encode())
while True:
    message = input(f"{username}: ")
    if message in kw_refresh:
        receive_message(client)
    elif message in kw_quit:
        close_connection(client)
        break
    else:
        send_message(client, message)
