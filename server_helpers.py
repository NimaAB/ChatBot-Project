import pickle


def broadcast_msg(message, persons):
    serialized_msg = pickle.dumps(message)
    for person in persons:
        persons[person].connection.send(serialized_msg)


def send_to_single_client(message, person):
    serialized_msg = pickle.dumps(message)
    person.connection.send(serialized_msg)


def new_conn_alert(person):
    info = f"{person.name} has joined the chat \n" \
           f" on address {person.address} ..."
    print(info)
