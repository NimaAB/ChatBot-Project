import argparse
import pickle
import socket
import threading
import time
import random

from bot.bot_chooser import pick_bot
from models.message import Message

description = "The client is responsible to connect to the server, write and read sockets to and from the " \
              "server.\nArguments are not required. If arguments are not given, then those will be sett to the " \
              "defaults. "
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-ip', '--ipaddr', metavar='', type=str, help='IPv4 flag')
parser.add_argument('-p', '--port', metavar='', type=int, help='Port for the connection the default port is 6000')
parser.add_argument('-bn', '--botname', metavar='', type=str, help='The name of bot which represents a client.\n'
                                                                   'Choose between those names (Alice, Bob, '
                                                                   'Dora and Chuck)')
args = parser.parse_args()


def arg_handlers(arguments) -> tuple:
    bots = ("Alice", "Bob", "Dora", "Chuck")

    if (not arguments.botname) or (arguments.botname.title() not in bots):
        username = random.choice(bots)
    else:
        username = arguments.botname.title()

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

conn_refused = [False]
DISCONNECT = Message(sender=USERNAME, content="BYE", content_type="CONNECTION")


def receive_msg(connection: socket):
    while True:
        try:
            received_msg = connection.recv(BUFFER_SIZE)
            if received_msg:
                message: Message = pickle.loads(received_msg)
            else:
                continue

            if message.sender == "Host":
                if message.content == "USERNAME":
                    connection.send(pickle.dumps(Message(sender=USERNAME, content_type="CONNECTION")))
                elif message.content_type == "CONN-SUCCEED":
                    print(f"{message.sender}: {message.content}")
                elif message.content_type == "DISCONNECT":
                    print(f"{message.sender}: {message.content}")
                elif message.content_type == "CONN_REFUSED":
                    print(f"{message.sender}: {message.content}")
                    connection.send(pickle.dumps(DISCONNECT))
                    conn_refused[0] = True
                    break
                else:
                    RECEIVED_MSGS_FROM_SERVER.append(message)
                    print(f"{message.sender}: {message.content}")
            else:
                RECEIVED_MSGS_FROM_BOTS.append(message)
                time.sleep(2)
                print(f"{message.sender}: {message.content}")

            if len(RECEIVED_MSGS_FROM_BOTS) == 4:
                connection.send(pickle.dumps(DISCONNECT))
                break
        except OSError as e:
            print(e)
            conn_refused[0] = True
            break
    connection.close()


def write_msg(connection: socket):
    while True:
        if len(RECEIVED_MSGS_FROM_SERVER) == 1:
            # print(len(RECEIVED_MSGS_FROM_SERVER))
            message = pick_bot(USERNAME, RECEIVED_MSGS_FROM_SERVER[0])
            serialized_msg = pickle.dumps(message)
            connection.send(serialized_msg)
            break
        elif conn_refused[0]:
            break
        else:
            continue


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
