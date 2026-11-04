# fonction de lancer_partie :
   # mettre le compteur de vagues à 1
   # indiquer que la partie est toujours en cours
   # récupérer la liste des monstres depuis la base de données
   # récupérer la liste des scores depuis la base de données
    
   # tant que le joueur n'a pas perdu :
       # choisir un monstre au hasard
       # afficher le numéro de la vague
       # afficher le nom et les caractéristiques du monstre
        
       # tant que le monstre et l'équipe sont encore en vie :
           # faire attaquer les personnages de l'équipe
           # vérifier si le monstre a encore des points de vie
           # si le monstre est vaincu :
               # afficher un message pour annoncer la victoire
               # passer à la vague suivante
               # arreter le combat en cours
           # sinon :
               # faire attaquer le monstre
            
           # vérifier si il reste des personnages en vie dans l'équipe
           # si toute l'équipe est éliminée :
               # indiquer que la partie est perdue
               # arreter la partie
                
   # enregistrer le score du joueur et afficher le classement


# fonction de tirer_monstre_aleatoire :
   # récupérer la liste des monstres dans la base de données
   # choisir un monstre au hasard dans la liste
   # renvoyer le monstre choisi avec ses caractéristiques


# fonction de gerer_attaques_equipe :
   # parcourir tous les personnages de l'équipe :
       # vérifier si le personnage est encore vivant
       # si c'est le cas :
           # calculer les dégats en prenant en compte son attaque et la défense du monstre
           # faire en sorte que les dégats soient au minimum de 1
           # retirer les dégats des points de vie du monstre
           # afficher un message pour dire que le personnage a attaqué


# fonction de gerer_attaque_monstre :
   # garder uniquement les personnages qui sont encore en vie
   # choisir au hasard un personnage parmi les survivants
   # calculer les dégats en tenant compte de l'attaque du monstre et de la défense du personnage
   # faire en sorte que les dégats soient au minimum de 1
   # retirer les dégats des points de vie du personnage
   # afficher un message pour dire que le monstre a attaqué


# fonction de verifier_equipe_vivante :
   # parcourir les personnages de l'équipe :
       # si un personnage a encore des points de vie :
           # retourner vrai car il reste au moins un survivant
   # si aucun personnage n'est encore en vie :
       # retourner faux


# fonction de traiter_fin_de_partie :
   # afficher le score final du joueur
   # préparer un dictionnaire avec le nom du joueur et le nombre de vagues atteintes
   # enregistrer le score dans la base de données MongoDB
   # récupérer les trois meilleurs scores, du plus élevé au plus faible
   # afficher le classement des trois meilleurs joueurs