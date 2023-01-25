import socket
import threading

name = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',5000))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "Welcome to the chat room. Please enter your name: ":
                name = input("Enter name: ")
                client.send(name.encode())
            # elif message == 'exit':
            #     print("disconnected")
            #     client.close()
            else:
                print(message)
            # client.close()
        except:
            client.close()
            break

def write():
    while True:
        msg = input("")
        message = f'{name} : {msg}'
        if msg == "exit":
            # client.send(cli_name.encode())
            print("disconnected")
            client.close()
            break
        else:
            client.send(message.encode())
    # client.close()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()