import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET refers to address from the internet it require pair of host and port number
#where the host can be url or  address and port number 
#SOCK_STREAM is used to create TCP protocols

s.bind((socket.gethostname(), 3457))
# it accepts 2 parameter host and port number
# gethostname() is used when server and client is on the same device
# 3456 port number greater than 1023 
# it is used to bind server with the client

s.listen(5)
# it is used to connect to a remote address

while True:
    clt, adr = s.accept()
    # to accept client socket and address
    print(f"Connection to {adr} established")
    # f string is literal string prefixed with f and contains py expression within ""
    clt.send(bytes("Socket programming in python","utf-8"))
    # after connection is established to pass the message
    # we are passing bytes so bytes type is specified
    clt.close()
