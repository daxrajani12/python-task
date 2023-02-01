import threading #for thread functions
import socket #to use socket modules

host = '127.0.0.1' #local host ip address
port = 4567 #port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create server socket object
server.bind((host,port)) #bind the server to host, and port
server.listen() #it is used to connect to a remote address

clients = [] #list to store client number 
cli_names = [] #list to store client name 
#both number and name will have same index value

def broadcast(message): #to send message to all client 
    for client in clients: #loop in clients list
        client.send(message) #sends the message to all the clients

def handle(client, address): #to handle the clients
    while True: #loop untill break is applied
        # try: #first it will be executed if error occur than except will be executed
        message = client.recv(1024).decode() #message received from on of the clients
            # if message == "exit":
            #     break
            # print(f"[{cli_name}] {message}")
            # message_send = input("enter message: ")
            # client.send(message_send.encode())
    # client.close()
            # broadcast(message) # broadcast function is called 
        # except: # if error occurs in the try than this will be executed
        index = clients.index(client)
        cli_name = cli_names[index]

        if message == "exit":    
            # index = clients.index(client) #will get the index from the list
            clients.remove(client) # will remove the client from clients list
            client.close() #close the client socket connection
            # cli_name = cli_names[index] #will get the name of client 
            broadcast(f'{cli_name} left the chat'.encode()) #broadcasts the message
            print(f'{cli_name} left the chat') #prints on server window
            cli_names.remove(cli_name) #removes the client name feom list
            break
        else:
            print(message)
            message_send = input("enter message: ")
            client.send(message_send.encode())

def receive(): #to accept the connection 
    while True:
        client, address = server.accept() #to accept client socket and address and establish the connection
        print(f"connected with {str(address)}") #print the client name and address on server

        client.send('cli'.encode()) #sends the cli key word so client send the name 
        cli_name = client.recv(1024).decode() #received the name form the client
        cli_names.append(cli_name) #client will be appended to the list
        clients.append(client) #client will be appended to the list

        print(f'Name of the client is {cli_name}') #prints the name of clie on server
        broadcast(f'{cli_name} joined the chat'.encode()) #message with client name will be broadcasted
        client.send('Connected to the server'.encode()) #message will be directly sent to the server

        thread = threading.Thread(target=handle, args=(client,address)) # parameter is set to handle function with client as the argument passed to the function. it will run hundle fun. in seperate thread
        thread.start() #starts the thread 

        # thread_recv = threading.Thread(target=receive, args=(client, address))
        # thread_recv.start()

print("Server is listening...")
receive()