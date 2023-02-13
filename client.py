import socket
from pickle import dumps,loads
x=socket.socket()
port=5000
host="127.0.0.1"
x.connect((host,port))
while(True):
    print("Enter data to send:")
    data=input()
    x.send(dumps(data))