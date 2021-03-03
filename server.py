import sys  # sys.argv will be afterwards
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6000
FORMAT = 'utf-8'
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)
MAX_USERS = 2

DISCONNECT_MSG = "BYE"

usernames = []
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(MAX_USERS)


def broadcast_msg(message):
    for client in clients:
        client.send(message)


def client_handler(client):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE)
            broadcast_msg(msg)
            print(msg.decode(FORMAT))
        except:
            disconnecting(client)
            break


def receive_msg():
    threads = []
    while True:
        client, address = server.accept()
        print(f"A client with address {address} connected to the server")

        client.send("USERNAME".encode(FORMAT))
        username = client.recv(BUFFER_SIZE).decode()
        usernames.append(username)
        clients.append(client)
        print(f"username of the client is {username}")
        print(f"The chat waiting for {MAX_USERS - len(clients)} client(s) to begin.")
        broadcast_msg(f"{username} joined the chat".encode(FORMAT))
        client.send("Your are now connected to the server".encode(FORMAT))
        thread = threading.Thread(target=client_handler, args=(client,))
        threads.append(thread)
        if len(clients) == MAX_USERS:
            for th in threads:
                th.start()
        else:
            continue


"""
def send_first_msg():
    if len(clients) == MAX_USERS:
        broadcast_msg("Hello everyone!".encode(FORMAT))
    else:
        broadcast_msg(f"The server is waiting for {MAX_USERS - len(clients)} more users to join the chat")
"""

print(f"SERVER LISTENING on {ADDRESS} ...")
receive_msg()


# helper methods:
def disconnecting(client):
    index = clients.index(client)
    clients.remove(client)
    username = usernames[index]
    usernames.remove(username)
    client.close()
    broadcast_msg(f"{username} has left the chat".encode(FORMAT))
