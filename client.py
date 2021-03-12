import argparse
import time
import socket
import threading
import pickle
from bot.chatbot import *
from models.message import Message

FORMAT = 'utf-8'
BUFFER_SIZE = 1024

parser = argparse.ArgumentParser(description="")
parser.add_argument('-ip', '--ipaddr', metavar='', type=str, required=True, help='IP-address flag is required')
parser.add_argument('-p', '--port', metavar='', type=int, help='Port for the connection the default port is 6000')
parser.add_argument('-bn', '--botname', metavar='', type=str, help='The name of bot which represents a client.\n'
                                                                   'Choose between those names (Alice, Bob, '
                                                                   'Dora and Chuck)')
args = parser.parse_args()

if args.botname:
    USERNAME = peak_bot(args.botname).sender
else:
    USERNAME = random.choice(BOTS)

if args.port:
    PORT = args.port
else:
    PORT = 6000

if args.ipaddr:
    HOST = args.ipaddr
else:
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
