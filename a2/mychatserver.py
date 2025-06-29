from socket import *
import threading

serverPort = 12345 # Port number

def accept_client(cnSocket, addr):
    print(f"New connection from ({addr})")
    cnList[cnSocket] = addr

    while True:
        try:
            msg = cnSocket.recv(1024).decode()
            if not msg:
                break

            print(f"{addr}: {msg}")

            relay_msg(cnSocket, addr, msg, cnList)
        except ConnectionResetError:
            break

def relay_msg(sender_socket, addr, msg, cnList):
    response = f'{addr}: {msg}'
    
    for cnSocket in cnList:
        if cnSocket != sender_socket:
            cnSocket.send(response.encode())

cnList = {}

serverSocket = socket(AF_INET, SOCK_STREAM)
# Create a TCP socket

serverSocket.bind(('', serverPort))
#Bind the socket to the port

serverSocket.listen(10)
# Listening for incoming connections

print(f"Server listening on 127.0.0.1:{serverPort}")

while True:
    # Accept connection
    cnSocket, addr = serverSocket.accept()
        
    t = threading.Thread(target=accept_client, args = (cnSocket, addr ))
    t.start()

