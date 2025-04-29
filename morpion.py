grille = {
    "A":['_','_','_'],
    "B":['_','_','_'],
    "C":['_','_','_']
}

def aff_grille(grille: dict) -> None:
    print(f"   | 1 | 2 | 3 |")
    for ligne , colonnes in grille.items():
        print(f" {ligne} | {colonnes[0]} | {colonnes[1]} | {colonnes[2]} |")

aff_grille(grille)
