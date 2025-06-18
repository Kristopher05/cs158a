from socket import *

serverport = 12000 # Port number

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverport))
#Bind the socket to the port

serverSocket.listen(1)
# Listening for incoming connections

while True:
    # Accept connection
    cnSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")
    
    #Receive connection
    message = cnSocket.recv(64).decode()

    # Process
    if len(message) >= 10:
        msg_len = message[:2]
        sentence = message[2:]
    else:
        msg_len = message[:1]
        sentence = message[:1]
    
    print(f"msg_len: {msg_len}")
    print(f"processed: {sentence}")
    print(f"msg_len_sent: {msg_len}")

    capSentence = sentence.upper()

    # Send
    cnSocket.send(capSentence.encode())

    # Close
    cnSocket.close()