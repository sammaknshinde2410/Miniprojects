#a client that sends and recieves messages save this code as chatclient.py

import socket
host = '127.0.0.1'
port = 9500

#create client side socket
s = socket.socket()
s.connect((host,port))

#enter data at client
str = input('Enter data : ')

#continue as long as exit not entered by user
while str != 'exit':
    #send data from client to server
    s.send(str.encode())

    #recieve the response data from server
    data = s.recv(1024)
    data = data.decode()
    print('From server: ' + data)


    #enter data
    str = input('Enter data: ')

#close connection
s.close()
