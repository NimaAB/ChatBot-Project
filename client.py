import sys
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.0.33',1024))
msg = clientSocket.recv(1024).decode()
print(msg)


