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

# Fonction pour afficher le classement
def voir_classement():
    print("\n-> Affichage du Top 3 des scores...")
    # TODO: recuperer et afficher les scores depuis mongodb
    pause()


# Fonction principale qui gere le programme et la boucle du menu
def main():
    db = connecter_db()
    print("Bienvenue dans le jeu de combat !")
    
    while True:
        afficher_menu()
        choix = demander_nombre(1, 3)
        
        if choix == 1:
            lancer_partie()
        elif choix == 2:
            voir_classement()
        elif choix == 3:
            print("\nMerci d'avoir joué, à bientôt !")
            break

# Verifier si on execute bien ce fichier directement
    # Lancer la fonction principale du programme