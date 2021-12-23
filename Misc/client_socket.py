#!/usr/bin/env python

import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 10010
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello World".encode('utf-8'), ADDR)
client.sendto("I'm Alive".encode('utf-8'), ADDR)
client.sendto("killit".encode('utf-8'), ADDR)

# client.connect(ADDR)

# name = input("Enter your name: ")
# client.send(name.encode('utf-8'))

# print(client.recv(1024).decode('utf-8'))
