# coding:utf-8 
# author:james
# datetime:2020/4/25 13:42
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "www.baidu.com"
client.connect((host,80))
client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format("/", host).encode("utf8"))

data = b""
while 1:
    d = client.recv(1024) #阻塞直到有數據
    if d:
        data += d
    else:
        break

data = data.decode("utf8")
print(data)