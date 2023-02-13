import socket
from pytesseract import pytesseract
from PIL import Image
from pickle import dumps,loads
text=""
x=socket.socket()
host="127.0.0.1"
port=8000
x.bind((host,port))
x.listen(5)
con,addr=x.accept()
print("connect",(addr))
file=open("processed_image.jpeg","wb")
image_data=con.recv(2048)
while image_data:
    file.write(image_data)
    image_data=con.recv(2048)
file.close()
def tesseract():
    path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path="processed_image.jpeg"
    pytesseract.tesseract_cmd=path
    text=pytesseract.image_to_string(Image.open(image_path))
    print(text)

tesseract()
x.close()
