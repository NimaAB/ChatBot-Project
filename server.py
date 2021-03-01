import sys #sys.argv will be afterwards
import socket
import threading


HOST = '192.168.0.33'
PORT = 6000
FORMAT = 'utf-8'
BUFFER_SIZE = 1024
ADDRESS = (HOST,PORT)

DISCONNECT_MSG = "Quit"

USERS = []
CLIENTS = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()

def broadcast_msg(message):
    for client in CLIENTS:
        client.send(message)

def client_handler(client):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE)
            broadcast_msg(msg)

        except:
            index = CLIENTS.index(client)
            CLIENTS.remove(index)
            client.close()
            username = USERS[index]
            broadcast_msg(f"{username} has left the chat")
            USERS.remove(index)
            break

def receive_msg():
    while True:
        client,address = server.accept()
        print(f"A client with address {address} connected to the server")
        client.send("USERNAME".encode(FORMAT))
        username = client.recv(BUFFER_SIZE).decode()
        USERS.append(username)
        CLIENTS.append(client)
        print(f"username of the client is {username}")
        broadcast_msg(f"{username} joined the chat".encode(FORMAT))
        client.send("Your are now connected to the server".encode(FORMAT))

        thread = threading.Thread(target=client_handler, args=(client,))
        thread.start()

print(f"SERVER LISTENING on {ADDRESS} ...")
receive_msg()