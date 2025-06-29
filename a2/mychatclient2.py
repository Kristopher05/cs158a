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
        try:
            # Receiving the modified sentence from the server
            response = clientSocket.recv(1024)

            if response:
                # Print the modified sentence
                print(response.decode())
            else:
                break
        except:
            break

# Loop to input messages
while True:
    # Input
    message = input()
    if message.lower() == 'exit':
        print(f"Disconnected from server")
        break
    
    # Creates a thread to start receiving messages from other clients
    t = threading.Thread(target=receive_message())
    t.start()

    # Sending message to the server
    clientSocket.send(message.encode())



# Close the socket
clientSocket.close()