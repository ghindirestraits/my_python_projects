#!/usr/bin/env python

import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 10010
ADDR = (HOST, PORT)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Created")

serversocket.bind(ADDR)

while True:
    packet, addr = serversocket.recvfrom(1024)

    print()
    print("Received ", packet.decode('utf-8'), "from ", addr)

    if packet.decode('utf-8') == "killit":
        break

serversocket.close()

# while True:
#     client, addr = serversocket.accept()
#     name = client.recv(1024).decode('utf-8')
#     print("Connected with ",  addr, name)

#     client.send("Welcome to Telusko".encode('utf-8'))

#     client.close()

#     if name == "hello":
#         print()
#         print("world")
#     else:
#         serversocket.close()
#         break
