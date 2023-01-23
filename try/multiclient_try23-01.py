import socket
import threading

cli_name = input("Enter name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',4567))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'cli':
                client.send(cli_name.encode())
            else:
                print(message)
        except:
            print("an error occured")
            client.close()
            break

def write():
    while True:
        msg = input("")
        if msg == "exit":
            client.send(cli_name.encode())
            client.close()
        message = f'{cli_name} : {msg}'
        
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()