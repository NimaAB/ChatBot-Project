import sys
import socket
import threading

HOST = '192.168.0.33'
PORT = 6000
ADDRESS = (HOST,PORT)
FORMAT = 'utf-8'
BUFFER_SIZE = 1024

DISCONNECT_MSG = "Server: Quit"
USERNAME = input("username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def receive_msg():
    while True:
        try:
            msg = client.recv(BUFFER_SIZE).decode(FORMAT)
            if msg == "USERNAME":
                client.send(USERNAME.encode(FORMAT))
            else:
                print(msg)
        except:
            print("SOMETHING FAILED!")
            client.close()
            break

def write_msg():
    while True:
        msg = f"{USERNAME}: {input()}"
        client.send(msg.encode(FORMAT))

receive_thread = threading.Thread(target=receive_msg)
receive_thread.start()

write_thread = threading.Thread(target=write_msg)
write_thread.start()