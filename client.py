import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 3457))

complete_info = '' #to terminate clinet. it allow to accept any information from server

while True: #to communicate until full message is received
    msg = s.recv(1024) #1024 is number of bytes to reveive from 
    # saving message which we have received

    if len(msg) <= 0: 
        break
    
    complete_info += msg.decode("utf-8")
    #since received message was encoded so it decodes using same bytes
print(complete_info)
   