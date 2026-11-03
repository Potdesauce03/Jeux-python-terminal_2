# on importe pymongo pour pouvoir parler avec la base de donnees
# on importe les fonctions utiles (demander nombre et pause) depuis utils

# fonction pour se connecter et recuperer la base de donnees
    # creer la connexion au serveur mongo en local sur le port de base
    # recuperer et retourner la base de donnees du jeu

# fonction pour afficher le menu principal
    # afficher une ligne de decoration
    # afficher le titre du jeu
    # afficher une ligne de decoration
    # afficher l'option 1
    # afficher l'option 2
    # afficher l'option 3

# fonction pour lancer une partie
    # afficher un petit message de debut
    # TODO: appeler la creation d'equipe et les combats (dans game.py)
    # faire une pause pour laisser le temps de lire

# fonction pour afficher le classement
    # afficher un message pour le top 3
    # TODO: recuperer et afficher les scores depuis mongodb
    # faire une pause pour laisser le temps de lire

# fonction principale qui gere le programme
    # recuperer la base de donnees en appelant la fonction de connexion
    # afficher le message de bienvenue au lancement
    
    # boucle infinie pour garder le menu actif tout le temps
        # appeler la fonction pour afficher le menu
        
        # demander et securiser le choix (entre 1 et 3)
        
        # si le joueur choisit 1
            # appeler la fonction pour lancer la partie
            
        # si le joueur choisit 2
            # appeler la fonction pour voir le classement
            
        # si le joueur choisit 3
            # afficher un message d'au revoir
            # couper la boucle avec break

# verifier si on execute bien ce fichier directement
    # lancer la fonction principale du programme