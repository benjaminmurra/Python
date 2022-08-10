#import socket module
from socket import *
import threading

class MultiThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address
        
    def run(self):
        while True:
            try:
                message = connectionSocket.recv(4096)
                #if no connection received, break.
                if not message:
                    break
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()    
				#Send one HTTP header line into socket
                connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n".encode())
                connectionSocket.send("\r\n".encode())  

                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

            except IOError:
				#Send response message for file not found
                connectionSocket.send("HTTP/1.1 404 Not Found \r\n Content-Type: text/html \r\n".encode())
                connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()) 

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM) 
    
    #Prepare a server socket
    serverPort = 80
    serverSocket.bind(("",serverPort))
    threads=[]

    #Server listens and threads are added to thread list
    while True :
        serverSocket.listen(5)
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        client_thread = MultiThread(connectionSocket,addr)
        client_thread.setDaemon(True)
        client_thread.start()
        threads.append(client_thread)

