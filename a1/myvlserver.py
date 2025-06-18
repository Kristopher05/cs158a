from socket import *

serverName = 'servername'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('Input lowercase sentence: ')

clientSocket.send(message.encode())

modifiedSentence = clientSocket.recv(64)

print('From Server: ', modifiedSentence.decode())