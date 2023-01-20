import socket #for socket modules

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

host = socket.gethostname() # get local machine name

port = 9876 #defined port number

s.connect((host, port)) # connection to hostname on the port. to connect client with server

while True: #untill break condition not appiled
    message = input("You: ") #getting message from client
    s.send(message.encode()) #sending message to server 
    if message == "q": #condition for exit message on client side
        print("disconnected")
        # s.send(message.encode()) #sending exit message to server so server will also get disconnected
        break
    received_message = s.recv(1024).decode() # message received from server
    if received_message == "q": #condition for exit message received from server
        # print("Server: %s" % received_message)
        print("server disconnected") 
        print("client disconnected")
        break
    print("Server: %s" % received_message) # received message is not exit message than to print it and continue the conversation

s.close() #to close the client socket
