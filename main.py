import pymongo
from utils import demander_nombre, pause


# fonction pour se connecter et recuperer la base de donnees
def connecter_db():
    client = pymongo.MongoClient("localhost", 27017)
    return client["jeu_combat"]


# fonction pour afficher le menu principal
def afficher_menu():
    print("   JEU DE COMBAT - TERMINAL - 2   ")
    print("1. Lancer une partie")
    print("2. Voir le classement")
    print("3. Quitter")


# Fonction pour lancer une partie
def lancer_partie():
    print("\n-> Lancement de la partie...")
    # TODO
    pause()


# fonction pour afficher le classement
def voir_classement():
    print("\n-> Le top 3")
    # TODO
    pause()


# fonction principale qui gere le programme et la boucle du menu
def main():
    db = connecter_db()
    print("Bienvenue dans le jeu")
    
    while True:
        afficher_menu()
        choix = demander_nombre(1, 3)
        
        if choix == 1:
            lancer_partie()
        elif choix == 2:
            voir_classement()
        elif choix == 3:
            print("\nMerci, à bientôt")
            break


# verification
if __name__ == "__main__":
    main()