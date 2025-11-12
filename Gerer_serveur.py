import socket

class GestionnaireIPPort:
    def __init__(self, base_ip="192.168.10.", ip_depart=1):
        """
        Initialise le gestionnaire.
        - base_ip : le début du réseau (ex: "192.168.10.")
        - ip_depart : premier numéro d'adresse (par défaut 1)
        """
        self.base_ip = base_ip
        self.prochaine_ip = ip_depart
        self.utilises = {}  # routeur -> (ip, port)

    def obtenir_ip_port(self, nom_routeur):
        """
        Attribue une adresse IP et un port libre à un routeur.
        Si le routeur en a déjà une, on la renvoie.
        """
        if nom_routeur in self.utilises:
            return self.utilises[nom_routeur]

        # Générer une nouvelle adresse IP unique
        ip = f"{self.base_ip}{self.prochaine_ip}"
        self.prochaine_ip += 1

        # Trouver un port libre automatiquement
        port = self._obtenir_port_libre()

        # Sauvegarder l'association
        self.utilises[nom_routeur] = (ip, port)
        return ip, port

    def _obtenir_port_libre(self):
        """
        Trouve un port libre en laissant le système choisir.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 0))  # Le port 0 dit au système d’en choisir un libre
        port = s.getsockname()[1]
        s.close()
        return port

    def afficher_tout(self):
        """
        Affiche toutes les adresses IP et ports attribués.
        """
        print("\n=== Liste des IP et ports attribués ===")
        for routeur, (ip, port) in self.utilises.items():
            print(f"{routeur} → {ip}:{port}")
