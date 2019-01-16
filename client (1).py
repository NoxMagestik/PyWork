import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("Please enter the first password")#
port = int(input("Please enter the second password"))

server.connect((ip, port))