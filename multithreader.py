
from socket import *
import _thread as thread
import time
import sys

def now():
    """
    returns the time of day
    """
    return time.ctime(time.time())

def handleClient(connection):
    """
    a client handler function
    """
    while True:
        data = connection.recv(1024).decode()
        print ("received  message = ", data)
        modified_message= data.upper()
        connection.send(modified_message.encode())
        if (data == "exit"):
            break
    connection.close()


def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    """
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    try:
        serverSocket.bind(('',serverPort))

    except:
        print("Bind failed. Error : ")
        sys.exit()
    serverSocket.listen(1)
    print ('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()
        print('Server connected by ', addr)
        print('at ', now())
        thread.start_new_thread(handleClient, (connectionSocket,))
    serverSocket.close()

if __name__ == '__main__':
    main()












