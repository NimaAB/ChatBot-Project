import sys
import time
import socket
import threading
from chatbot import *

system_params = sys.argv
USERNAME = ""
PORT = 6000
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

if len(system_params) <= 1:
    USERNAME = random.choice(PERSONS)
else:
    PORT = int(sys.argv[1])
    USERNAME = sys.argv[2]

HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

# USERNAME = input("username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def receive_msg():
    while True:
        msg = client.recv(BUFFER_SIZE).decode(FORMAT)
        if msg == "USERNAME":
            client.send(USERNAME.encode(FORMAT))
        elif msg == "QUIT":
            break
        else:
            print(msg)


def write_msg():
    i = 0
    while i <= 1:
        msg = f"{USERNAME}: {peak_bot(USERNAME)}"
        client.send(msg.encode(FORMAT))
        input()
        i += 1


receive_thread = threading.Thread(target=receive_msg)
receive_thread.start()

write_thread = threading.Thread(target=write_msg)
write_thread.start()

