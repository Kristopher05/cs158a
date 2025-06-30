from socket import *
import threading

serverName = 'localhost' # IP address
serverPort = 12345        # Port number

# TCP SOCKET_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to the server
clientSocket.connect((serverName, serverPort))
print("Connected to chat server. Type 'exit' to leave.")

# Function to receive messages
def receive_message():
    while True:
        # Receiving the modified sentence from the server
        response = clientSocket.recv(1024)

        if response:
            # Print the modified sentence
            print(response.decode())

# Creates a thread to start receiving messages from other clients
t = threading.Thread(target=receive_message, daemon=True)
t.start()

# Loop to input messages
while True:
    # Input
    message = input()

    # Exits the server if the client types exit
    if message.lower() == 'exit':
        print(f"Disconnected from server")
        break

    # Sending message to the server
    clientSocket.send(message.encode())



# Close the socket
clientSocket.close()