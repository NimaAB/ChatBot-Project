import argparse
import time
import socket
import threading
import pickle
from bot.chatbot import *
from models.message import Message

BOTS = ["Alice", "Bob", "Dora", "Chuck"]
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

parser = argparse.ArgumentParser(description="")
parser.add_argument('-ip', '--ipaddr', metavar='', type=str, required=False, help='IP-address flag is required')
parser.add_argument('-p', '--port', metavar='', type=int, help='Port for the connection the default port is 6000')
parser.add_argument('-bn', '--botname', metavar='', type=str, help='The name of bot which represents a client.\n'
                                                                   'Choose between those names (Alice, Bob, '
                                                                   'Dora and Chuck)')
args = parser.parse_args()

if (not args.botname) or (args.botname not in BOTS):
    USERNAME = random.choice(BOTS)
else:
    USERNAME = args.botname

if args.port:
    PORT = args.port
else:
    PORT = 6000

if args.ipaddr:
    HOST = args.ipaddr
else:
    HOST = socket.gethostbyname(socket.gethostname())

ADDRESS = (HOST, PORT)

RECEIVED_MSGS = []


def receive_msg(connection: socket):
    while True:
        received_msg = connection.recv(BUFFER_SIZE)
        message: Message = pickle.loads(received_msg)
        # print(message)

        if message.content == "USERNAME" and message.sender == "Host":
            connection.send(pickle.dumps(Message(sender=USERNAME, message_type="CONNECTION")))
        elif message.message_type == "CONNECTION":
            print(f"{message.sender}: {message.content}")
        else:
            RECEIVED_MSGS.append(message)
            print(f"{message.sender}: {message.content}")


def write_msg(connection: socket):

    while True:
        time.sleep(2.0)
        if len(RECEIVED_MSGS) < 1:
            continue
        else:
            message = peak_bot(USERNAME, RECEIVED_MSGS[len(RECEIVED_MSGS)-1])
            serialized_msg = pickle.dumps(message)
            connection.send(serialized_msg)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

receive_thread = threading.Thread(target=receive_msg, args=(client,))
receive_thread.start()

write_thread = threading.Thread(target=write_msg, args=(client,))
write_thread.start()
