#import socket module
from socket import *
import sys
serverPort=80
serverSocket = socket(AF_INET, SOCK_STREAM)

#Fill in start
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
#Fill in end

while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())  # Empty line
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:

        #Send response message for file not found
        # Fill in start
        print("404 Page Not Found")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())  
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    serverSocket.close()
    sys.exit()

