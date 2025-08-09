import socket
import ssl

host = 'www.google.com'
port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
secure_sock = context.wrap_socket(sock, server_hostname=host)
secure_sock.connect((host, port))

secure_sock.sendall(f'GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n'.encode("utf-8"))

response = ""

while True:
    data = secure_sock.recv(4096).decode()
    if not data:
        break
    response += data

idx = response.find('\r\n\r\n') + 4
html_response = response[idx:]

with open("response.html", "w") as f:
    f.write(html_response)

secure_sock.close()