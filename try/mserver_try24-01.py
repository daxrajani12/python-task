import socket
import threading

# List to keep track of clients
clients = []
client_names = []

def broadcast(message, sender):
    """Broadcast a message to all clients"""
    for client in clients:
        client.send(sender.encode() + b': ' + message)

def handle(client):
    """Handle a single client connection"""
    name = client.recv(1024).decode()
    client_names.append(name)
    clients.append(client)
    broadcast(name + " has joined the chat room.", name)
    while True:
        message = client.recv(1024)
        if message:
            broadcast(message, name)
        else:
            client.close()
            clients.remove(client)
            client_names.remove(name)
            broadcast(name + " has left the chat room.", name)
            break

def main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print("Server is running...")
    while True:
        client, address = s.accept()
        print(f"Client connected: {str(address)}")
        client.send("Welcome to the chat room. Please enter your name: ".encode())
        client_thread = threading.Thread(target=handle, args=(client,))
        client_thread.start()

if __name__ == '__main__':
    main()
