import socket
import threading

# Function for handling multiple clients
def client_thread(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        broadcast_data(data)
    conn.close()

# Function for broadcasting data to all clients
def broadcast_data(data):
    for client in clients:
        client.send(data)
        data = ''

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9876
server.bind((host,port))
server.listen(5)

# List to keep track of all clients
clients = []

# Accept connections and start a new thread for each client
while True:
    conn, addr = server.accept()
    clients.append(conn)
    print("Client connected: " + str(addr))
    threading.Thread(target=client_thread, args=(conn, addr)).start()
