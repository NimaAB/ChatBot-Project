import sys  # sys.argv will be afterwards
import socket
import threading
import pickle
import time

from models.message import Message
from models.person import Person
from server_helpers import *

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6000
FORMAT = 'utf-8'
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)
MAX_USERS = 2  # will changed to 4

persons = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(MAX_USERS)


def client_handler(connection):
    while True:
        try:
            message = connection.recv(BUFFER_SIZE)
            deserialized_msg = pickle.loads(message)
            print(deserialized_msg)
            broadcast_msg(deserialized_msg, persons)
            print(f"{deserialized_msg.sender}: {deserialized_msg.content}")
        except:
            # disconnecting(person)
            connection.close()
            break


def receive_msg():
    threads = []
    while True:
        client, address = server.accept()
        client.send(pickle.dumps(Message(sender="Host", content="USERNAME")))
        username = pickle.loads(client.recv(BUFFER_SIZE)).sender

        person = Person(name=username, address=address, connection=client)
        persons.append(person)
        new_conn_alert(person)

        ret_message = Message(sender="Host", content=f"{username} joined the chat")
        broadcast_msg(ret_message, persons)

        connection_confirmed_msg = Message(sender="Host", content="Your are now connected to the server")
        send_to_single_client(connection_confirmed_msg, person)

        thread = threading.Thread(target=client_handler, args=(person.connection,))
        threads.append(thread)

        if len(persons) == MAX_USERS:
            for th in threads:
                th.start()
                time.sleep(2.0)
        else:
            print(f"The chat waiting for {MAX_USERS - len(persons)} client(s) to begin.")  # not sure yet
            continue


print(f"SERVER LISTENING on {ADDRESS} ...")
receive_msg()
