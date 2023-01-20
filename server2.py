import socket #for socket modules

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

host = socket.gethostname() # get local machine name

port = 9999 #defined port number

s.bind((host, port)) # bind the socket to host, and a port

s.listen(1) # become a server socket

print("Waiting for a client...") 
flag = 0
while True: #until break is applied
    
    clientsocket, addr = s.accept()# establish a connection

    print("Got a connection from %s" % str(addr))

    while True: #untill brek is applied

            message = clientsocket.recv(1024).decode() #message received from client 
            
            if message == "q": #condition for exit message received from client
                print("Client disconnected")
                flag = 1 # making flag 1 to apply socket close fun. outside loop
                clientsocket.close() #closing connection with client socket
                break
                # s.close()
                # s.shutdown(socket.SHUT_RDWR)
                
                
            else:
                print("Received: %s" % message) #exit message is not received than continue the conversation
                message_send = input("Server: ") #getting message from server
                clientsocket.send(message_send.encode()) # sending message to client
                if message_send == "q": #checking condition for exit message input from server side
                    # print("disconnect")
                    flag = 1 #making flag 1 to apply socket close fun. outside loop
                    clientsocket.close() #closing connection with client socket
                    break
                    # s.close()
                    # s.shutdown(socket.SHUT_RDWR)
    if flag == 1: #check condition to break the loop
        break

if flag == 1: #checking condition to close server socket
    print("server disconnected ")
    s.close() #making server socket close
    # s.shutdown(socket.SHUT_RDWR)
