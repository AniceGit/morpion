grille = {
    "A":['_','_','_'],
    "B":['_','_','_'],
    "C":['_','_','_']
}

def aff_grille(grille: dict) -> None:
    print(f"   | 1 | 2 | 3 |")
    for ligne , colonnes in grille.items():
        print(f" {ligne} | {colonnes[0]} | {colonnes[1]} | {colonnes[2]} |")

def jouer_coup(grille: dict, joueur: str, coup: tuple)-> None:
    grille[coup[0]][coup[1]-1] = joueur 




def est_coup_valide(position:tuple, grille:dict) -> bool:
    colonne, ligne = position
    if grille[colonne][ligne] == '_' :
        return True
    else :
        return False
    
aff_grille(grille)
