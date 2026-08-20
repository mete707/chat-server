import socket
import threading
import os

PORT = int(os.environ.get("PORT", 10000))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', PORT))
server.listen()

clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            for client in clients:
                if client != client_socket:
                    client.send(msg)
        except:
            break
    clients.remove(client_socket)
    client_socket.close()

print(f"Sunucu {PORT} portunda bulutta çalışıyor...")
while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
