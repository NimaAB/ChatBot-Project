import argparse
import socket
import threading
import pickle
import time
from models.message import Message
from models.person import Person
from server_helpers import *
from bot.bots import me

parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', '--port', metavar='', type=int, help='Port for the connection the default port is 6000')
args = parser.parse_args()


def args_handler(arguments) -> int:
    if arguments.port:
        port = arguments.port
    else:
        port = 6000
    return port


# Global_variables:
# Connection
IPADDR = socket.gethostbyname(socket.gethostname())
PORT = args_handler(args)
ADDRESS = (IPADDR, PORT)


# Global_constants:
MAX_USERS = 2  # will be changed to 4
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

# Connection information messages:
CONN_CONFIRMATION = Message(sender="Host", content="Your are now connected to the server", content_type="CONNECTION")
# DISCONNECTING = Message(sender="Host", content="QUIT", content_type="CONNECTION")
CONNECTING = Message(sender="Host", content="USERNAME", content_type="CONNECTION")

# Clients that have been connected:
persons = []


def client_handler(connection):
    while True:
        message = connection.recv(BUFFER_SIZE)
        deserialized_msg = pickle.loads(message)
        broadcast_msg(deserialized_msg, persons)
        print(f"{deserialized_msg.sender}: {deserialized_msg.content}")


def receive_msg():
    threads = []
    while True:
        client, address = server.accept()   # accepting a connection
        client.send(pickle.dumps(CONNECTING))   # sending a connection message to get back the bot_name
        username = pickle.loads(client.recv(BUFFER_SIZE)).sender

        person = Person(name=username, address=address, connection=client)  # creating a Person object
        persons.append(person)
        new_conn_alert(person)  # a print out message just for the server

        send_to_single_client(CONN_CONFIRMATION, person)    # sending the connection confirmation back to the client

        # creating new thread for handling the client
        thread = threading.Thread(target=client_handler, args=(person.connection,))
        threads.append(thread)  # adding the thread to a list of threads

        # if all the bots are connected, then the chat begins with a suggestion message from the server
        if len(persons) == MAX_USERS:
            time.sleep(1)
            suggested_msg = me()  # there is a simple bot function that decides the first message
            print(f"{suggested_msg.sender}: {suggested_msg.content}")
            broadcast_msg(suggested_msg, persons)   # sends the message to all the bots
            break
        else:
            print(f"The chat waiting for {MAX_USERS - len(persons)} client(s) to begin.")  # not sure yet
            continue

    # after connection loop the client handler_threads will begin.
    for th in threads:
        th.start()
        time.sleep(2.0)


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a tcp_socket
    server.bind(ADDRESS)  # binding it to the address
    server.listen(MAX_USERS)  # making a queue for MAX_USERS to connect.

    print(f"SERVER LISTENING on {ADDRESS} ...")
    receive_msg()  # executing the main function of the server
