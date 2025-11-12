import socket
import threading

HOST = 'localhost'
PORT = 5000
client_ip = "192.168.10.2"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"Client {client_ip} connecté au serveur")

def recevoir_messages():
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except:
            break

# Thread pour recevoir les messages en continu
threading.Thread(target=recevoir_messages, daemon=True).start()

while True:
    msg = input()
    s.send(f"{client_ip}: {msg}".encode('utf-8'))
    if msg.lower() in ["bye", "arret"]:
        break
    if 
s.close()
