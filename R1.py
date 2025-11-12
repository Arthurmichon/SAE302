import socket
import threading

clients = {}  # dictionnaire: nom_client -> connexion

def gerer_client(conn, client_name):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8')
            print(f"Message reçu de {client_name}: {msg}")

            # On envoie le message à tous les autres clients sauf l'expéditeur
            for name, c in clients.items():
                if name != client_name:
                    c.send(f"{client_name}: {msg}".encode('utf-8'))
            if msg.lower() == "arret":
                conn.close()

        except:
            break
    print(f"{client_name} déconnecté")
    del clients[client_name]
    conn.close()

# Création du serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 5000))
s.listen(5)
print("Serveur démarré sur 0.0.0.0:5000")

while True:
    conn, addr = s.accept()
    client_name = conn.recv(1024).decode('utf-8')  # Le client envoie son nom/IP simulée
    print(f"{client_name} connecté")
    clients[client_name] = conn
    threading.Thread(target=gerer_client, args=(conn, client_name), daemon=True).start()
