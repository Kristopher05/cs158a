#Variable-Length Message TCP Client-Server

'server.py': Runs the TCP server and listens for clients and processes messages
'client.py': Sends a lowercase string starting with 2 integers that equal to the amount of characters in the string and then displays the capitalized response
'README.py': Project description and usage

Example:
Client Side:
Input lowercase sentence: 10helloworld
From Server: HELLOWORLD

Server Side:
Connected from 10.0.0.2
msg_len: 10
processed: helloworld
meg_len_sent: 10
Connection closed
