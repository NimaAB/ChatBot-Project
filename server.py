import sys
import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('192.168.0.33',1024))

serverSocket.listen(5)

while True: 
    (clientSocket,address) = serverSocket.accept()
    clientSocket.send(f"You are now connenctet to {address}".encode())
    msg_back = clientSocket.recv(1024).decode() 
    print(msg_back)

    #q = input("write Q to Quit: " )
    #if q=="Q":
        #break
