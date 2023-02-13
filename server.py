import socket,threading
from pickle import loads,dumps
def recv_data_client():
    global con,connected
    while(connected):
        data=con.recv(1000)
        print("Received data",con,loads(data))
x=socket.socket()
port=5000
host="127.0.0.1"
x.bind((host,port))
x.listen(5)
con,addr=x.accept()
connected=True
t=threading.Thread(target=recv_data_client())
t.start()
print("This is main function")
x.close()
