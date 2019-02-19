# -*- coding: utf-8 -*-
import socket
def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("localhost",8001))
    sock.listen(5)

    while True:
        connection,addr = sock.accept()
        buf = connection.recv(1024)
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
        connection.send(b"No No No")
        connection.close()

if __name__=="__main__":
    main()