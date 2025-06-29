from socket import *

serverName = 'localhost' # IP address
serverPort = 12345        # Port number

# TCP SOCKET_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to the server
clientSocket.connect((serverName, serverPort))
print("Connected to chat server. Type 'exit' to leave.")

while True:
    # Input
    message = input()
    if message.lower() == 'exit':
        print(f"Disconnected from server")
        break

    # Sending message to the server
    clientSocket.send(message.encode())

    # Receiving the modified sentence from the server
    response = clientSocket.recv(1024)

    # Print the modified sentence
    print(response.decode())

# Close the socket
clientSocket.close()