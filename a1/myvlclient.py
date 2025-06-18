from socket import *

serverport = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverport))

serverSocket.listen(1)

while True:
    cnSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    sentence = cnSocket.recv(64).decode()

    capSentence = sentence.upper()

    cnSocket.send(capSentence.encode())

    cnSocket.close()