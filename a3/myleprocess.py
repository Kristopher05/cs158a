import threading
from socket import *
import time
import uuid
import json

class Message:
    def __init__(self, uuid_val, flag):
        self.uuid = uuid_val
        self.flag = flag

    def to_json(self):
        return json.dumps({
            "uuid": str(self.uuid),
            "flag": self.flag
        }) + "\n"
    
    def from_json(data):
        obj = json.loads(data)
        return Message(uuid.UUID(obj["uuid"]), obj["flag"])
    
def read_config():
    with open("config.txt", "r") as f:
        lines = f.readlines()
        serverip, serverport = lines[0].strip().split(',')
        clientip, clientport = lines[1].strip().split(',')
        return (serverip, int(serverport)), (clientip, int(clientport))
    
def log_event(prefix, msg, comparison=None, state=None, leader=None):
    with open("log.txt", "a") as f:
        f.write(f"{prefix: uuid={msg.uuid}, flag={msg.flag}}")
        if comparison:
            f.write(f", {comparison}")
        if state is not None:
            f.write(f", state={state}")
        if leader:
            f.write(f", leader_id={leader}")
        f.write("\n")

class Node:
    def __init__(self, serverAddr, clientAddr):
        self.uuid = self.uuid4()
        self.state = 0
        self.leaderId = None
        self.serverAddr = serverAddr
        self.clientAddr = clientAddr
        self.clientSoc = None
        self.conn = None
        self.running = True
    
    def start_server(self):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', self.serverAddr))
        serverSocket.listen(1)
        print(f"Server listening on {self.serverAddr}")
        self.conn = serverSocket.accept
        threading.Thread(target=self.readMessages, deaemon=True).start()
    
    def readMessages(self):
        buffer = ''
        while self.running:
            try:
                data = self.conn.recv(1024).decode()
                if not data:
                    break
                buffer += data
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    msg = Message.from_json(line)
                    self.handle_msg(msg)
            except Exception as e:
                break
    def handle_msg(self, msg):
        if msg.uuid > self.uuid:
            comp = "greater"
        elif msg.uuid < self.uuid:
            comp = "less"
        else:
            comp = "same"
        
        if self.state == 1:
            log_event("Received", msg, comp, self.state, self.leaderId)
            if msg.flag == 0:
                log_event("Ignored", msg)
                return
            elif msg.flag== 1 and msg.uuid == self.leaderId:
                self.running = False
                return
        else:
            log_event("Received", msg, comp, self.state)
            if msg.flag == 0:
                if msg.uuid == self.uuid:
                    self.state = 1
                    self.leaderId = self.uuid
                    print(f"Leader is decided to {self.uuid}")
                    leader_msg = Message(self.uuid, 1)
                    self.send_message(leader_msg)
                    log_event("Sent", leader_msg)
                elif msg.uuid > self.uuid:
                    self.send_message(msg)
                else:
                    log_event
            elif msg.flag == 1:
                self.state = 1
                self.leaderId = msg.uuid
                self.send_message(msg)
                log_event("Sent", msg)
    
    def send_message(self, msg):
        self.clientSoc.sendall(msg.to_json().encode())
        log_event("Sent", msg)
    
    def connectNext(self):
        while True:
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect(self.clientAddr)
                self.clientSoc = s
                break
            except:
                time.sleep(1)
    
    def run(self):
        threading.Thread(target=self.start_server, daemon=True).start()
        time.sleep(2)
        self.connectNext()
        time.sleep(2)
        initial_msg = Message(self.uuid,0)
        self.send_message(initial_msg)

        while self.running:
            time.sleep(1)

        print(f"Leader is {self.leaderId}")