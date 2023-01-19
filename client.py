import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to create socket of sclient
#AF_INET refers to address from the internet it require pair of host and port number
#where the host can be url or  address and port number 
#SOCK_STREAM is used to create TCP protocols


s.connect((socket.gethostname(), 3457))
#to connect client with server 
# gethostname() is used when server and client is on the same device
# port number greater than 1023 

complete_info = '' #to terminate clinet. it allow to accept any information from server

while True: #to communicate until full message is received
    msg = s.recv(1024) #1024 is number of bytes to reveive from 
    # saving message which we have received

    if len(msg) <= 0: 
        break
    
    complete_info += msg.decode("utf-8")
    #since received message was encoded so it decodes using same bytes
print(complete_info)
   