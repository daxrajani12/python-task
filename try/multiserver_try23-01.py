import threading
import socket

host = '127.0.0.1' #local host
port = 4567 #port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
cli_names = []

def broadcast(message):
    for client in clients:
        # if clients.index() != client:
        #     continue
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # if message == cli_name:
            #     broadcast(f'{cli_name} left the chat'.encode())
            #     index = cli_names[cli_name]
            #     cli_names.remove(cli_name)
            #     clients.remove(index)
            #     client.close()
            # else:    
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            cli_name = cli_names[index]
            broadcast(f'{cli_name} left the chat'.encode())
            print(f'{cli_name} left the chat')
            cli_names.remove(cli_name)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('cli'.encode())
        cli_name = client.recv(1024).decode()
        cli_names.append(cli_name)
        clients.append(client)

        print(f'Name of the client is {cli_name}')
        broadcast(f'{cli_name} joined the chat'.encode())
        client.send('Connected to the server'.encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()