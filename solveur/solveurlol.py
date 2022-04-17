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

nb_essais=0
nb=0
#Propose un mot
def prop(motslongueur,bonnes,mal,fausses,dejapropose,nb_essais,nb):
    malponctuel=[]
    bonnesponctuel=[]
    faussesponctuel=[]
    proposition=trouveurmot(motslongueur,dejapropose,[],nb_essais)
    dejapropose.append(proposition)
    print(proposition)

    demande=input("Alors ? \n")
    if demande=='-1':
        print("Trouvé! en {} propositions".format(nb+1))
        return 0
    demandelist=list(demande)
    #print(demandelist)
    
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
    prop(motslongueur,bonnes,mal,fausses,dejapropose,nb_essais+1,nb+1)

prop(motslongueur,bonnes,mal,fausses,dejapropose,nb_essais,nb)


#Validation



#il y a un probleme avec rideau par exemple, le résultat dépend du sens dans lequel on met la séquence de chiffre