from longueurmots import *
from compteuroccurence import *
from trouveurmot import *
from transformateur import *

#Demande la longueur du mot
longueur=int(input("Longueur du mot : \n"))  #on demande la longueur à l'utilisateur
motslongueur=longueurmots(longueur)             # on récupere tous les mots de cette longueur
#print("motslongueur",motslongueur)



dejapropose=[]
fausses=[]
bonnes=[]
mal=[]


#Propose un mot
def prop(motslongueur,bonnes,mal,fausses,dejapropose):
    malponctuel=[]
    bonnesponctuel=[]
    faussesponctuel=[]
    proposition=trouveurmot(motslongueur,dejapropose)
    dejapropose.append(proposition)
    print(proposition)

    demande=input("Alors ? \n")
    if demande=='-1':
        print("Trouvé!")
        return 0
    demandelist=list(demande)
    print(demandelist)
    
    for i in range(len(demandelist)):               #on ajoute les lettres et les emplacements au bons endroit
        if demandelist[i]=='2':
            bonnes.append((proposition[i],i))
            bonnesponctuel.append((proposition[i],i))
        elif demandelist[i]=='1':
            mal.append((proposition[i],i))
            malponctuel.append((proposition[i],i))
        else:
            fausses.append(proposition[i])
            faussesponctuel.append(proposition[i])

    motslongueur=transformation(motslongueur,bonnes,mal,fausses,bonnesponctuel,malponctuel,faussesponctuel)
    #print(motslongueur)
    prop(motslongueur,bonnes,mal,fausses,dejapropose)

prop(motslongueur,bonnes,mal,fausses,dejapropose)


#Validation

