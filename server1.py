import socket #to creates sockets
import pickle #used to serializing and deserializing a python obj. structure

a=10 #some header size
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to create socket of server
#AF_INET refers to address from the internet it require pair of host and port number
#where the host can be url or  address and port number 
#SOCK_STREAM is used to create TCP protocols

s.bind((socket.gethostname(),4455)) #binding tuples
# it accepts 2 parameter host and port number
# gethostname() is used when server and client is on the same device
# 3456 port number greater than 1023 
# it is used to bind server with the client

s.listen(5)
# it is used to connect to a remote address
#() in it we define backlog parameter. 
#it specifies the number of unaccepted connections that the system will allow before refusing new connection

while True:
    clt, adr = s.accept()
    # to accept client socket and address
    print(f"Connection to {adr} established")
    # f string is literal string prefixed with f and contains py expression within ""
    
    m={1:"Clients", 2:"Server"}
    mymsg = pickle.dumps(m) #the msg we want to print later
    #dictonary "m" used dumps method available in pickle module 
    #to serialize this object "m"(dictonary)
    mymsg = bytes(f'{len(mymsg):<{a}}',"utf-8") + mymsg
    #incrementing mymsg and sending using "send method"

    clt.send(mymsg)
    # after connection is established to pass the message
    # we are passing bytes so bytes type is specified
    # clt.close() #to close communication
