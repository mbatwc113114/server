import socket
import threading
ip = "47.251.17.186"
port = 9999
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connection to server
client.connect((ip,port))
nick = input("enter nickname ")
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nick.encode('ascii'))
            else:
                print(message)
        except:
            print("connection stopped....")
            client.close()
            

def write():
    while True:
        message = f"{nick} : {input('')}"
        client.send(message.encode('ascii'))
                    
receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)
                    

receive_thread.start()
write_thread.start()
