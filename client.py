import argparse
import pickle
import socket
import threading
import time

from bot.chatbot import *
from models.message import Message

parser = argparse.ArgumentParser(description="")
parser.add_argument('-ip', '--ipaddr', metavar='', type=str, help='IPv4 flag')
parser.add_argument('-p', '--port', metavar='', type=int, help='Port for the connection the default port is 6000')
parser.add_argument('-bn', '--botname', metavar='', type=str, help='The name of bot which represents a client.\n'
                                                                   'Choose between those names (Alice, Bob, '
                                                                   'Dora and Chuck)')
args = parser.parse_args()


def arg_handlers(arguments) -> tuple:
    bots = ("Alice", "Bob", "Dora", "Chuck")
    if (not arguments.botname) or (arguments.botname not in bots):
        username = random.choice(bots)
    else:
        username = arguments.botname

    if arguments.port:
        port = arguments.port
    else:
        port = 6000

    if arguments.ipaddr:
        ipaddress = arguments.ipaddr
    else:
        ipaddress = socket.gethostbyname(socket.gethostname())

    return username, ipaddress, port


# GLOBALS:
# Connection
USERNAME, IPADDR, PORT = arg_handlers(args)
ADDRESS = (IPADDR, PORT)

# Message:
FORMAT = 'utf-8'
BUFFER_SIZE = 1024
RECEIVED_MSGS_FROM_SERVER = []
RECEIVED_MSGS_FROM_BOTS = []

DISCONNECT = Message(sender=USERNAME, content="BYE", content_type="CONNECTION")


def receive_msg(connection: socket):
    while True:
        try:
            received_msg = connection.recv(BUFFER_SIZE)
            message: Message = pickle.loads(received_msg)
            if message.content == "USERNAME" and message.sender == "Host":
                connection.send(pickle.dumps(Message(sender=USERNAME, content_type="CONNECTION")))
                print("first if\n")
            elif message.content_type == "CONNECTION":
                print(f"{message.sender}: {message.content}")
                print("second if\n")
            elif message.sender == "Host" and message.content_type == "CHAT":
                print("third if\n")
                RECEIVED_MSGS_FROM_SERVER.append(message)
                print(f"{message.sender}: {message.content}")
            else:
                RECEIVED_MSGS_FROM_BOTS.append(message)
                print("forth if\n")
                print(f"{message.sender}: {message.content}")
        except OSError as e:
            print(e)
            break


def write_msg(connection: socket):

    for _ in range(3):
        time.sleep(4.0)
        print(len(RECEIVED_MSGS_FROM_SERVER))
        if len(RECEIVED_MSGS_FROM_SERVER) == 1:
            message = peak_bot(USERNAME, RECEIVED_MSGS_FROM_SERVER[0])
            serialized_msg = pickle.dumps(message)
            connection.send(serialized_msg)


if __name__ == "__main__":
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDRESS)
        receive_thread = threading.Thread(target=receive_msg, args=(client,))
        receive_thread.start()
        write_thread = threading.Thread(target=write_msg, args=(client,))
        write_thread.start()
    except ConnectionRefusedError:
        print(f"You can't connect to the chatroom.\n Cause: No server is bind to address:{ADDRESS} not running")
