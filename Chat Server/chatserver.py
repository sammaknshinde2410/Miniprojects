# a server that recieves and sends messages save this as chatserver.py

import socket
host = "127.0.0.1"
port = 9500


#create server side socket
s = socket.socket()
s.bind((host,port))

#let maximum no. of connections are 1 only
s.listen()

#wait till a client connects
c, addr = s.accept()
print('A client connected')


#server runs continously
while True:
    #recieved data from client
    data = c.recv(1024)

    #if client sends empty string,come out
    if not data:
        break
    print('From client: '+ str(data.decode()))

    #enter response data from server
    data1 = input('Enter response: ')

    #send that data to client
    c.send(data1.encode())

    #send that data to client
#close connection
c.close()


