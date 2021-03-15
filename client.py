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
RECEIVED_MSGS = []

DISCONNECT = Message(sender=USERNAME, content="BYE", content_type="CONNECTION")


def receive_msg(connection: socket):
    while True:
        try:
            received_msg = connection.recv(BUFFER_SIZE)
            message: Message = pickle.loads(received_msg)
            if message.content == "USERNAME" and message.sender == "Host":
                connection.send(pickle.dumps(Message(sender=USERNAME, content_type="CONNECTION")))
                print("first if\n", message)
            elif message.content_type == "CONNECTION":
                print(f"{message.sender}: {message.content}")
                print("second if\n", message)
            else:
                print("third if\n", message)
                RECEIVED_MSGS.append(message)
                print(f"{message.sender}: {message.content}")
        except OSError as e:
            print("You are now disconnected")
            break


def write_msg(connection: socket):
    while True:
        time.sleep(2.0)
        if len(RECEIVED_MSGS) < 1:
            continue
        elif len(RECEIVED_MSGS) > 2:
            connection.send(pickle.dumps(DISCONNECT))
            connection.close()
            break
        else:
            message = peak_bot(USERNAME, RECEIVED_MSGS[len(RECEIVED_MSGS) - 1])
            serialized_msg = pickle.dumps(message)
            connection.send(serialized_msg)


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)

    receive_thread = threading.Thread(target=receive_msg, args=(client,))
    receive_thread.start()

    write_thread = threading.Thread(target=write_msg, args=(client,))
    write_thread.start()
