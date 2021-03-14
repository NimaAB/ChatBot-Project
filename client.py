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
parser.add_argument('-ip', '--ipaddr', metavar='', type=str, required=False, help='IP-address flag is required')
parser.add_argument('-p', '--port', metavar='', type=int, help='Port for the connection the default port is 6000')
parser.add_argument('-bn', '--botname', metavar='', type=str, help='The name of bot which represents a client.\n'
                                                                   'Choose between those names (Alice, Bob, '
                                                                   'Dora and Chuck)')
args = parser.parse_args()

if args.botname:
    USERNAME = args.botname
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

MSGS_FROM_SERVER = []


def receive_msg(connection: socket):
    while True:
        received_msg = connection.recv(BUFFER_SIZE)
        message: Message = pickle.loads(received_msg)
        # print(message)

        if message.content == "USERNAME" and message.sender == "Host":
            connection.send(pickle.dumps(Message(sender=USERNAME)))
        elif message.sender == 'Host' and message.content != "USERNAME":
            print(f"{message.sender}: {message.content}")
            MSGS_FROM_SERVER.append(message)
        else:
            print(f"{message.sender}: {message.content}")


def write_msg(connection: socket):
    for _ in range(1):
        time.sleep(2.0)
        message = peak_bot(USERNAME, MSGS_FROM_SERVER[0])
        # MY_MSGS.append(message)
        serialized_msg = pickle.dumps(message)
        connection.send(serialized_msg)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

receive_thread = threading.Thread(target=receive_msg, args=(client,))
receive_thread.start()

write_thread = threading.Thread(target=write_msg, args=(client,))
write_thread.start()
