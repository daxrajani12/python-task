import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind the socket to a public host, and a port
s.bind((host, port))

# become a server socket
s.listen(1)

print("Waiting for a client...")

while True:
    # establish a connection
    clientsocket, addr = s.accept()

    print("Got a connection from %s" % str(addr))

    while True:

            message = clientsocket.recv(1024).decode()
            
            if message == "q":
                print("Client disconnected")
                clientsocket.close()
                # break
                # s.close()
                # s.shutdown(socket.SHUT_RDWR)
                
                break
            else:
                print("Received: %s" % message)
                message_send = input("Server: ")
                clientsocket.send(message_send.encode())
                if message_send == "q":
                    print("disconnect")
                    clientsocket.close()
                    s.close()
                    s.shutdown(socket.SHUT_RDWR)
