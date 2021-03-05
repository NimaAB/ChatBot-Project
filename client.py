import sys
import time
import socket
import threading
import pickle
from bot.chatbot import *
from models.message import Message

system_params = sys.argv
PORT = 6000  # default port
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

if len(system_params) <= 1:
    USERNAME = random.choice(BOTS)
else:
    PORT = int(system_params[1])
    USERNAME = peak_bot(system_params[2]).sender

HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)


def receive_msg(connection):
    while True:
        received_msg = connection.recv(BUFFER_SIZE)
        # print(type(received_msg))
        message: Message = pickle.loads(received_msg)
        # print(type(message))
        # print(message.content)

        if message.content == "USERNAME" and message.sender == "Host":
            connection.send(pickle.dumps(Message(sender=USERNAME)))
        else:
            print(f"{message.sender}: {message.content}")


def write_msg(connection):
    for _ in range(1):
        time.sleep(2.0)
        message = peak_bot(USERNAME)
        serialized_msg = pickle.dumps(message)
        connection.send(serialized_msg)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

receive_thread = threading.Thread(target=receive_msg, args=(client,))
receive_thread.start()

write_thread = threading.Thread(target=write_msg, args=(client,))
write_thread.start()
