from longueurmots import *
from compteuroccurence import *
from trouveurmot import *
from transformateur import *

#Demande la longueur du mot
longueur=int(input("Longueur du mot : \n"))  #on demande la longueur à l'utilisateur
motslongueur=longueurmots(longueur)             # on récupere tous les mots de cette longueur
motslongueur=transformateur(motslongueur)
    #print(motslongueur)



dejapropose=[]
lettrefausses=[]

#Propose un mot
print(trouveurmot(motslongueur))


#Validation

