import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

while True:
    message = input("You: ")
    s.send(message.encode())
    if message == "q":
        print("disconnected")
        s.send(message.encode())
        break
    received_message = s.recv(1024).decode()
    if received_message == "q":
        print("Server: %s" % received_message)
        print("disconnected")
        break
    print("Server: %s" % received_message)

s.close()
