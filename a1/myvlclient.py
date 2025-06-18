from socket import *

serverport = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverport))

serverSocket.listen(1)
print(f'The server is ready to receive')

while True:
    cnSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")
    

    message = cnSocket.recv(64).decode()

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

    cnSocket.send(capSentence.encode())

    cnSocket.close()