import socket
import threading
import time

HOST = '10.49.232.96'
PORT = 2000
client_name = input("Entrez votre nom ou IP simulée : ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(client_name.encode('utf-8'))  # On envoie l'identifiant au serveur


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
print("Pour arrêter le serveur écrire 'arret'\nPour arrêter le client écrire 'bye'")
while True:

    msg = input()
    s.send(msg.encode('utf-8'))
    if msg.lower() in ["bye", "arret"]:
        break

s.close()
