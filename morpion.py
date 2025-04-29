grille = {
    "A":['_','_','_'],
    "B":['_','_','_'],
    "C":['_','_','_']
}
grille2 = {
    "A":['X','X','X'],
    "B":['O','O','X'],
    "C":['O','X','O']
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
            #print("gagnant:",est_gagnant(grille), est_gagnant(grille)=="")
            if est_gagnant(grille)!="":
                break
    
    print("Partie terminée")
    gagnant = est_gagnant(grille)
    if gagnant:
        print(f"Le gagnant est : {gagnant}")
    else :
        print("Match nul")

def est_pleine(grille:dict) -> bool:
    est_pleine = True
    for ligne in grille :
        for celulle in grille[ligne] :
            if celulle == "_":
                est_pleine = False
                return est_pleine
    return est_pleine

def est_gagnant (grille:dict) -> str:
    valeur_gagnante = ""
    # #contrôle des lignes
    for ligne in grille:
        if len(set(grille[ligne]))==1 and grille[ligne][0]!="_":
            valeur_gagnante = grille[ligne][0]
            return valeur_gagnante
        
    # #contrôle des colonnes
    col1=[]
    col2=[]
    col3=[]
    for ligne in grille.values():
        col1.append(ligne[0])
        col2.append(ligne[1])
        col3.append(ligne[2])
    if len(set(col1)) == 1 and ligne[0]!="_":
        valeur_gagnante = col1[0]
        return valeur_gagnante
    if len(set(col2)) == 1 and ligne[0]!="_":
        valeur_gagnante = col2[0]
        return valeur_gagnante
    if len(set(col3)) == 1 and ligne[0]!="_":
        valeur_gagnante = col3[0]
        return valeur_gagnante
    
    #contrôle des diagonales
    diag1=[]
    diag2=[]
    for ligne, liste in grille.items():
        if ligne == "A":
            diag1.append(liste[0])
            diag2.append(liste[2])
        if ligne == "B":
            diag1.append(liste[1])
            diag2.append(liste[1])
        if ligne == "C":
            diag1.append(liste[2])
            diag2.append(liste[0])
    if len(set(diag1)) == 1 and liste[0]!="_":
        valeur_gagnante = diag1[0]
        return valeur_gagnante
    if len(set(diag2)) == 1 and liste[0]!="_":
        valeur_gagnante = diag2[0]
        return valeur_gagnante
    return valeur_gagnante
jouer(grille)
# est_gagnant(grille)
#print(est_gagnant(grille), est_gagnant(grille) is None)