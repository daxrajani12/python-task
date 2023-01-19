import socket #to creates sockets
import pickle #used to serializing and deserializing a python obj. structure

a=10 #some header size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to create socket of sclient
#AF_INET refers to address from the internet it require pair of host and port number
#where the host can be url or  address and port number 
#SOCK_STREAM is used to create TCP protocols

s.connect((socket.gethostname(), 4455))
#to connect client with server 
# gethostname() is used when server and client is on the same device
# port number greater than 1023 

while True:
    complete_info = b'' #we are receiving info in bytes so specified b''(b with empty strign)
    rec_msg = True #msg is received is true
    while True:
        mymsg = s.recv(16) #while it is true it will receive 16bytes per transfer
        if rec_msg: #
            print(f"The length of message = {mymsg[:a]}")
            x = int(mymsg[:a])
            rec_msg = False #when full msg received is completed it will be set false
        complete_info += mymsg #if not then it will be incremented and next chunk of message will be received
        if len(complete_info)-a == x: #if complete info is received is equal to length of messagage originally present at the server side
            print("Received the complete info") #msg of complete msg revceived
            print(complete_info[a:])
            m = pickle.loads(complete_info[a:])
            #to deserialise the message loads is used passing the complete info received from server
            print(m) #printing message that received from server
            rec_msg = True 
            complete_info = b''
    print(complete_info)