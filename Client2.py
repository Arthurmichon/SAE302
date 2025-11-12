import socket
import threading
import sys

HOST = 'localhost'
PORT = 5000
client_ip = "192.168.10.2"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"Client {client_ip} connecté au serveur")

# Envoyer le nom/ip simulé au serveur pour l'identification
s.send(client_ip.encode('utf-8'))

stop_threads = False  # variable globale pour arrêter le thread


def recevoir_messages():
    global stop_threads
    while not stop_threads:
        try:
            data = s.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8')
            print(msg)

            # Si on reçoit "arret", on ferme tout
            if "arret" in msg.lower():
                print("Message 'arret' reçu — fermeture du client.")
                stop_threads = True
                break
        except:
            break


# Thread pour recevoir les messages en continu
threading.Thread(target=recevoir_messages, daemon=True).start()

while True:
    msg = input()
    s.send(f"{client_ip}: {msg}".encode('utf-8'))
    if msg.lower() in ["bye", "arret"]:
        stop_threads = True
        break

s.close()
print("Client arrêté.")
