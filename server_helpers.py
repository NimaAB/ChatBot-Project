import pickle

"""
This file contains helper methods for the server.py
"""


def broadcast_msg(message, persons):
    serialized_msg = pickle.dumps(message)
    for person in persons:
        person.connection.send(serialized_msg)


def send_to_single_client(message, person):
    serialized_msg = pickle.dumps(message)
    person.connection.send(serialized_msg)


# TODO: Writing the method below!!
"""
def disconnecting(person):
    index = persons.index(person)
    person.connection.close()
    message = pickle.dumps(Message(sender="Host", content=f"{person.name} has left the chat"))
    broadcast_msg(message)
"""


def new_conn_alert(person):
    info = f"{person.name} has joined the chat \n" \
           f" on address {person.address} ..."
    print(info)
