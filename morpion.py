grille = {
    "A":['_','_','_'],
    "B":['_','_','_'],
    "C":['_','_','_']
}

def afficher_grille(grille: dict) -> None:
    for ligne, colonnes in grille.items():
        print(f"{colonnes}")

afficher_grille(grille)
