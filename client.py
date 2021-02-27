import sys
import socket
from chatbot import peak_bot

PERSONS = ["Alice", "Bob", "Dora", "Chuck"]

if len(sys.argv)==1:
    person = None 
else:
    person = sys.argv[1]

msg_to_send = peak_bot(person)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.0.33',1024))
msg = clientSocket.recv(1024).decode()
print(msg)

clientSocket.send(msg_to_send.encode())


