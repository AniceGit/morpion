# grille = {
#     "A":['_','_','_'],
#     "B":['_','_','_'],
#     "C":['_','_','_']
# }
grille = {
    "A":['X','O','X'],
    "B":['O','O','X'],
    "C":['X','X','_']
}

def aff_grille(grille: dict) -> None:
    print(f"   | 1 | 2 | 3 |")
    for ligne , colonnes in grille.items():
        print(f" {ligne} | {colonnes[0]} | {colonnes[1]} | {colonnes[2]} |")

def jouer_coup(grille: dict, joueur: str, coup: tuple)-> bool:
    if est_coup_valide((coup), grille):
        grille[coup[0]][coup[1]-1] = joueur 
        return True
    else :
        print("OH ! Coup Invalide !")
        return False

def est_coup_valide(position:tuple, grille:dict) -> bool:
    ligne, colonne = position
    if grille[ligne][colonne-1] == '_' :
        return True
    else :
        return False
    
def jouer(grille: dict) -> str:
    while est_pleine(grille) == False:
        ligne = input("Ligne :")
        colonne = int(input("Colonne :"))
        lettre = input("Lettre :")
        coup = (ligne, colonne)
        if jouer_coup(grille, lettre, coup):
            aff_grille(grille)
    else :
        print("Partie terminée")

def est_pleine(grille:dict) -> bool:
    est_pleine = True
    for ligne in grille :
        for celulle in grille[ligne] :
            if celulle == "_":
                est_pleine = False
                return est_pleine
    return est_pleine
        
jouer(grille)
