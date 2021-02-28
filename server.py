import sys #sys.argv will be afterwards
import socket
import threading


HOST = '192.168.0.33'
PORT = 6000
FORMAT = 'utf-8'
BUFFER_SIZE = 1024
ADDRESS = (HOST,PORT)

DISCONNECT_MSG = "Quit"

THREADS = []
CONNECTIONS = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def client_handler(connection,address):
    print(f"<NEW CONNECTION> {address} connected.")
    connected = True
    while connected:
        msg = connection.recv(BUFFER_SIZE).decode(FORMAT)
        print(msg)
        return_msg = input(f"Server: ")
        if return_msg == DISCONNECT_MSG:
            connected = False

        connection.send(f"Server: {return_msg}".encode(FORMAT))
    connection.close()



def start_connection():
    server.listen()
    print(f"<LISTENING> Server listening {HOST} ...")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=client_handler,args=(conn,addr))
        thread.start()
        CONNECTIONS.append((conn,addr))
        THREADS.append(thread)
        print(f"<ACTIVE CONNECTIONS> {threading.activeCount()-1}")



print("<STARTING> server is starting ...")
start_connection()

#for th in THREADS:
#   th.join()
