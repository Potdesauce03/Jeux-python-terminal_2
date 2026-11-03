import pymongo
from utils import demander_nombre, pause


# Fonction pour se connecter et recuperer la base de donnees
def connecter_db():
    client = pymongo.MongoClient("localhost", 27017)
    return client["jeu_combat_terminal_v2"]


# Fonction pour afficher le menu principal
def afficher_menu():
    print("\n==============================")
    print("   JEU DE COMBAT - TERMINAL - V2   ")
    print("==============================")
    print("1. Lancer une partie")
    print("2. Voir le classement (Top 3)")
    print("3. Quitter")


# Fonction pour lancer une partie
def lancer_partie():
    print("\n-> Lancement de la partie...")
    # TODO: appeler la creation d'equipe et les combats (dans game.py)
    pause()


# Fonction pour afficher le classement
def voir_classement():
    print("\n-> Affichage du Top 3 des scores...")
    # TODO: recuperer et afficher les scores depuis mongodb
    pause()

# Fonction principale qui gere le programme
    # Recuperer la base de donnees grace a la fonction de connexion
    # Afficher le message de bienvenue du jeu
    
    # Boucle infinie pour garder le menu actif
        # Afficher le menu principal a l'ecran
        
        # Demander et securiser le choix de l'utilisateur (entre 1 et 3)
        
        # Si le choix est 1
            # Appeler la fonction pour lancer la partie
            
        # Si le choix est 2
            # Appeler la fonction pour voir le classement
            
        # Si le choix est 3
            # Afficher le message d'au revoir
            # Quitter la boucle avec break

# Verifier si on execute bien ce fichier directement
    # Lancer la fonction principale du programme