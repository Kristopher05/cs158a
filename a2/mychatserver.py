from socket import *
import threading

serverPort = 12345 # Port number

def accept_client(cnSocket, addr):
    print(f"New connection from ({addr})")

    # Grabs the port number from the address
    cnPort = addr[1]

    # Inserts the address into the list
    cnList[cnSocket] = addr

    #  Decodes the message for the server to read
    while True:
        msg = cnSocket.recv(1024).decode()
            
        # Prints for the server
        print(f"{cnPort}: {msg}")
            
        # Sends the message to the other clients
        relay_msg(cnSocket, cnPort, msg, cnList)

# Function to send messages to other clients
def relay_msg(sender_socket, cnPort, msg, cnList):
    response = f'{cnPort}: {msg}'
    
    # Sends the response to every socket in the list
    for cnSocket in cnList:
        if cnSocket != sender_socket:
            cnSocket.send(response.encode())

# List for connection sockets
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
    
    # Thread to accept multiple clients
    t = threading.Thread(target=accept_client, args = (cnSocket, addr ), daemon=True)
    t.start()

