import socket #for socket modules
import threading #to use thread and for thred functions

cli_name = input("Enter name: ") #getting client name from the user

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
client.connect(('127.0.0.1',4567)) #connection with server on ip and port number

def receive(): #function for receiving message from the server
    while True: #loop unless break is applied
        try: #to execute described fun if error occue than except will execute
            message = client.recv(1024).decode() #message received from the server
            if message == 'cli': # checking if cli is received than it will sned the client name
                client.send(cli_name.encode()) #sending client name
            else:   #else printing the message 
                print(message) #print message received from the server
        except: #if error occur in try this will be executed
            client.close() #it closes the client
            break

def write(): #function to get message from client and send that message to server
    while True: #loop unless break is applied
        msg = input("") #get message from the client
        message = f'{cli_name} : {msg}' #attaching message with client name
        if msg == "exit":  #if message is exit than it will close the client socket
            print("disconnected") 
            client.close() #to close client socket
            break
        else:
            client.send(message.encode()) #sends the message to server

receive_thread = threading.Thread(target=receive) #thread for receive function
receive_thread.start() #started the thread

write_thread = threading.Thread(target=write) #thread for wite function
write_thread.start() #started the thread