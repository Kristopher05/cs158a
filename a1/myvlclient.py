from socket import *

serverName = 'localhost' # IP address
serverPort = 12000        # Port number

# TCP SOCKET_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to the server
clientSocket.connect((serverName, serverPort))

# Input
message = input('Input lowercase sentence: ')

# Sending message to the server
clientSocket.send(message.encode())

# Receiving the modified sentence from the server
modifiedSentence = clientSocket.recv(64)

# Print the modified sentence
print('From Server: ', modifiedSentence.decode())
# Close the socket
clientSocket.close()