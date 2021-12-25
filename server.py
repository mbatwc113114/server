import socket
import threading
ip = "47.251.17.186"
port = 55555
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
clients = []
nicknames = []

server.listen()

def aloud(message):
    for client in clients:
        client.send(message.encode("ascii"))
        
def handel(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            aloud(message)
            
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            aloud('{} left'.format(nickname))
            break

def receive_client():
    while True:
        
        client, address = server.accept()
        print("connected with {}".format(address))
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        aloud("{} joined!".format(nickname))
        handel_thread = threading.Thread(target=handel, args=(client,))
        handel_thread.start()
if __name__ == "__main__":
    receive_client()
        
