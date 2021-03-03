import sys
import time
import socket
import threading
import json
from bot.chatbot import *
from models.message import Message

system_params = sys.argv
USERNAME = ""
PORT = 6000     # default port
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

if len(system_params) <= 1:
    USERNAME = random.choice(PERSONS)
else:
    PORT = int(system_params[1])
    USERNAME = peak_person(system_params[2])

HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def receive_msg():
    while True:
        msg = client.recv(BUFFER_SIZE).decode(FORMAT)
        msg_dict = json.loads(msg)
        message = Message(msg_dict["sender"],)
        if msg == "USERNAME":
            client.send(USERNAME.encode(FORMAT))
        elif msg == "QUIT":
            break
        else:
            print(msg)


def write_msg():
    for _ in range(1):
        message = peak_bot(USERNAME)
        msg = f"{USERNAME}: {message}"
        client.send(msg.encode(FORMAT))
        time.sleep(3.0)


receive_thread = threading.Thread(target=receive_msg)
receive_thread.start()

write_thread = threading.Thread(target=write_msg)
write_thread.start()

