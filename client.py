import sys
import socket

USER = sys.argv[1]

HOST = '192.168.0.33'
PORT = 6000
ADDRESS = (HOST,PORT)
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

DISCONNECT_MSG = "Server: Quit"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send_msg(msg):
    message = msg.encode()
    client.send(message)

def recv_msg():
    return client.recv(BUFFER_SIZE).decode(FORMAT)

while True:
    msg_input = input(f"{USER}: ")
    msg_to_send = f"{USER}: {msg_input}"
    send_msg(msg_to_send)
    recvd_msg = recv_msg()
    print(recvd_msg)
    if recvd_msg == DISCONNECT_MSG:
        break

client.close()