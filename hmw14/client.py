import socket


SRV_HOST = "127.0.0.1"
SRV_PORT = 6969

username = input("Please, enter your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SRV_HOST, SRV_PORT))


client.send(f"'{username}' joined the chat".encode())
while True:
    message = input(f"{username}: ")
    if message in ("r", "refresh"):
        print(client.recv(2048).decode())
    elif message in (r"\q", r"\quit", r"\exit"):
        client.send(f"{username} has left the chat".encode())
        client.close()
        break
    else:
        client.send(f"{username}: {message}".encode())
