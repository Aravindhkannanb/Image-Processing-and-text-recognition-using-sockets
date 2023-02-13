import socket
import cv2
from pickle import loads,dumps
host="127.0.0.1"
port=8000
x=socket.socket()
x.connect((host,port))
cam=cv2.VideoCapture(0)
while(True):
    ret,image=cam.read()
    cv2.imshow("image",image)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    cv2.imwrite("apple.png",image)
file=open("apple.png","rb")
image_data=file.read(2048)
while image_data:
    x.send(image_data)
    image_data=file.read(2048)
file.close()
x.close()