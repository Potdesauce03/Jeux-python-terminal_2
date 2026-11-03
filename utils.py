def demander_nombre(min_val, max_val):
    while True:
        entree = input(f"Votre Choix (entre {min_val} et {max_val}) :")

        if entree.isdigit():
            nombre = int(entree)
            if min_val <= nombre <= max_val:
                return nombre
            else:
                print(f"Ce numéro n'exist pas, vous devez prendre un numero comprix entre {min_val} et {max_val}.")
        else:
            print("Vous devez entrez uniquement un chiffre.")

def pause():
    input("\nAppuyez sur entrée pour continuer...")
