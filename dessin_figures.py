# -*- coding:utf-8 -*
import os


def trace_quadrilatere(dim1,dim2,motif):    # Cette fonction permet de dessinner un rectangle ou carre par affichage recurssif du caractere "motif"
    ligne=""
    for i in range(dim1):
        ligne+=motif+"  "
    for i in range(dim2):
        print(ligne)

def triangle_trapeze(categorie_elt,taile_elt,taille_debut_affichage_elt,motif):     # Cette fonction concerne le trace des triangles et trapezes
    ligne=""
    for i in range(2*taile_elt):
        if categorie_elt.lower() in ["a","rectangle"]:
            ligne+=motif+" "    
            if i>=taille_debut_affichage_elt: print("\t",ligne)
        elif categorie_elt.lower() in ["b","isocele"]:
            marge=[(2*taile_elt-i)*" "]
            ligne=[(i+1)*(motif+" ")]
            if i>=taille_debut_affichage_elt: print(marge[0]+ligne[0])
        elif categorie_elt.lower() in ["c","quelconque"]:
            marge=[(2*taile_elt-i)*"   "]
            ligne=[(i+1)*(motif+" ")]
            if i>=taille_debut_affichage_elt: print(marge[0]+ligne[0])




# Explications relatives au fonctionnement du programme

print("\nce programme  vous permet de dessiner une figure de votre choix parmi celles qui vous sont proposees.\n\n".upper().center(150))
print("""   Figures possibles:
                                1- Carre
                                2- Rectangle
                                3- Triangle : a) Rectangle | b) Isocele | c) Quelconque 
                                4- Losange : a) Regulier | b) Irregulier 
                                5- Parallelegramme
                                6- Trapeze: a) Rectangle | b) Isocele | c) Quelconque 
                                7- Autres : a) Hexagone 
      """)
# Choix de la figure a dessiner par l'utilisateur ( Ainsi que du motif de dessin )

figure=str(input("Quel figure avez-vous choisit? (Entrer un nom ou un numero suivant la liste ci-dessus!)   "))

while figure.upper() not in ["1","CARRE","2","RECTANGLE","3","TRIANGLE","4","LOSANGE","5","PARALLELOGRAMME","6","TRAPEZE","7","AUTRES"]:
    figure=str(input("Cette figure ne figure pas dans notre liste. Entrer quelque-chose de correct:    "))

motif=""
while len(motif)!=1:
    motif=str(input("Entrer un seul caractere quelconque qui servira de motif pour votre schema:     "))

#############################################################3
print("\nPour le choix des dimensions, veillez entrer des valeurs entieres, positives et differentes de '0'.\n")
#############################################################3

# Code a executer si la figure choisie est un carre

if figure.upper() in ["1","CARRE"]:
    cote_carre=0
    while cote_carre<=0:
        try: cote_carre=int(input("Entrer une valeur representant la mesure du cote de votre carre:  "))
        except ValueError: 
            print("Nous attendons un nombre entier")
            cote_carre=0
        else:
            if cote_carre<=0: print("Le nombre attendu doit etre superieur a '0'.")
    trace_quadrilatere(cote_carre,cote_carre,motif)

# Code a executer si la figure choisie est un rectangle

elif figure.upper() in ["2","RECTANGLE"]:
    (longueur_rect,largeur_rect)=(0,0)
    while longueur_rect<=1 or largeur_rect<=0 or longueur_rect<=largeur_rect:
        try: (longueur_rect,largeur_rect)=(int(input("Entrer une valeur representant la longueur de votre rectangle:  ")),int(input("Entrer une valeur representant la largeur de votre rectangle:  ")))
        except ValueError: 
            print("Nous n'attendons que des valeurs entieres")
            (longueur_rect,largeur_rect)=(0,0)
        else:
            if longueur_rect<=1 or largeur_rect<=0: print("La plus petite valeur de la longueur est '2'; et celle de la largeur est '1'.")
            else: print("Votre longueur ne doit pas etre plus petite ou egale a votre largeur puisqu'il s'agit d'un rectangle")
    trace_quadrilatere(longueur_rect,largeur_rect,motif)
    
# Code a executer si la figure choisie est un triangle

elif figure.upper() in ["3","TRIANGLE"]:
    forme_triangle=str(input("Quelle categorie de triangle voulez-vous representer?:     ")) 
    while forme_triangle.lower() not in ["a","rectangle","b","isocele","c","quelconque"]:
        forme_triangle=str(input("Entrer une valeur correcte ( Referez-vous a la liste d'en haut ci necessaire ):     ")) 
    hauteur_triangle=1
    while hauteur_triangle<=1:
        try: hauteur_triangle=int(input("Entrer une valeur representant la hauteur de votre triangle:  "))
        except ValueError: 
            print("Nous attendons un nombre entier")
            hauteur_triangle=1
        else:
            if hauteur_triangle<=1: print("Le nombre attendu doit etre superieur a '1'.")
    triangle_trapeze(forme_triangle,hauteur_triangle,0,motif)

# Code a executer si la figure choisie est un losange

elif figure.upper() in ["4","LOSANGE"]:
    forme_losange=str(input("Quelle categorie de losange voulez-vous representer?:     ")) 
    while forme_losange.lower() not in ["a","regulier","b","irregulier"]:
        forme_losange=str(input("Entrer une valeur correcte ( Referez-vous a la liste d'en haut ci necessaire ):     ")) 
    hauteur_losange=2
    while hauteur_losange<=2:
        try: hauteur_losange=int(input("Entrer une valeur representant la mesure d'une diagonale de votre losange:  "))
        except ValueError: 
            print("Nous attendons un nombre entier")
            hauteur_losange=2
        else:
            if hauteur_losange<=2: print("Le nombre attendu doit etre superieur a '2'.")
    ligne=""
    if hauteur_losange%2==0: hauteur_losange+=1
    j=0
    for i in range(hauteur_losange):
        if forme_losange.lower() in ["a","regulier"]:
            if i<=hauteur_losange//2:
                marge=[(hauteur_losange//2-i)*"  "]
                ligne=[(i+1)*(motif+"   ")]
                print(marge[0]+ligne[0])
            else:
                j+=1
                marge=[(i-hauteur_losange//2)*"  "]
                ligne=[(i-2*j+1)*(motif+"   ")]
                print(marge[0]+ligne[0])
        elif forme_losange.lower() in ["b","irregulier"]:
            if i<=hauteur_losange//2:
                marge=[(hauteur_losange//2-i)*"  "]
                ligne=[(i+1)*(motif+"     ")]
                print(marge[0]+ligne[0])
            else:
                j+=1
                marge=[(i-hauteur_losange//2)*"  "]
                ligne=[(i-2*j+1)*(motif+"     ")]
                print(marge[0]+ligne[0])

# Code a executer si la figure choisie est un parallelogramme

elif figure.upper() in ["5","PARALLELOGRAMME"]:
    (longueur_para,largeur_para)=(0,0)
    while longueur_para<=1 or largeur_para<=0 or longueur_para<=largeur_para:
        try: (longueur_para,largeur_para)=(int(input("Entrer une valeur representant le plus long cote de votre paralllelogramme:  ")),int(input("Entrer une valeur representant le plus court cote de votre paralllelogramme:  ")))
        except ValueError: 
            print("Nous n'attendons que des valeurs entieres")
            (longueur_para,largeur_para)=(0,0)
        else:
            if longueur_para<=1 or largeur_para<=0: print("La plus petite valeur du plus long cote est '2'; et celle du plus court cote  est '1'.")
            else: print("Votre pluis long cote ne peut pas etre plus petit ou egal a votre plus court cote puisqu'il s'agit d'un parallelogramme")
    ligne=""
    marge=""
    for i in range(longueur_para):
        ligne+=motif+"  "
    for i in range(largeur_para):
        marge+=" "
        print(marge+ligne)

# Code a executer si la figure choisie est un trapeze

elif figure.upper() in ["6","TRAPEZE"]:
    forme_trapeze=str(input("Quelle categorie de trapeze voulez-vous representer?:     ")) 
    while forme_trapeze.lower() not in ["a","rectangle","b","isocele","c","quelconque"]:
        forme_trapeze=str(input("Entrer une valeur correcte ( Referez-vous a la liste d'en haut ci necessaire ):     ")) 
    hauteur_trapeze=1
    while hauteur_trapeze<=1:
        try: hauteur_trapeze=int(input("Entrer une valeur representant la hauteur de votre trapeze:  "))
        except ValueError: 
            print("Nous attendons un nombre entier")
            hauteur_trapeze=1
        else:
            if hauteur_trapeze<=1: print("Le nombre attendu doit etre superieur a '1'.")
    triangle_trapeze(forme_trapeze,hauteur_trapeze,hauteur_trapeze,motif)

# Code a executer si la figure choisie est "autres"

elif figure.upper() in ["7","AUTRES"]:
    choix_autres=str(input("Pour laquelle des trois figures de ce volet optez-vous?:     ")) 
    while choix_autres.lower() not in ["a","hexagone","b","octogone","c","cercle"]:
        choix_autres=str(input("Entrer une valeur correcte ( Referez-vous a la liste d'en haut ci necessaire ):     ")) 
    hauteur_autres=2
    while hauteur_autres<=2:
        try: hauteur_autres=int(input("Entrer une valeur representant la hauteur de votre figure:  "))
        except ValueError: 
            print("Nous attendons un nombre entier")
            hauteur_autres=2
        else:
            if hauteur_autres<=2: print("Le nombre attendu doit etre superieur a '2'.")
    ligne=""
    if hauteur_autres%2==0: hauteur_autres+=1
    j=0
    for i in range(hauteur_autres):
        if choix_autres.lower() in ["a","hexagone"]:
            if i<=hauteur_autres//3:
                marge=[(hauteur_autres//3-i)*"  "]
                ligne=[(i+1)*(motif+"   ")]
                print(marge[0]+ligne[0])
            elif hauteur_autres//3<i<=2*hauteur_autres//3:
                print(marge[0]+ligne[0])
            else:
                j+=1
                marge=[(i-2*hauteur_autres//3)*"  "]
                ligne=[(hauteur_autres//3-j+1)*(motif+"   ")]
                print(marge[0]+ligne[0])

os.system("pause")