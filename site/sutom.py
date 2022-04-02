import copy as cp

mot=input("Rentrer le mot a trouver : \n")    #demande du mot à l'utilisateur

MOT = list(mot)                             #on transforme le mot en liste de caractères
longueur=len(MOT)                           #on stock la longueur du mot
print(MOT)
global bonnes                               #on stock les lettres trouvées et bien placées dans bonnes
bonnes = ['-' for i in range(longueur)]     #on initialise cette liste
global nb_essais
nb_essais=0
def prop(MOT,longueur):                     #fonction prenant en argument le mot à deviner sous forme de liste de lettre et sa longueur               
    global bonnes
    propo=input("Proposition ({} lettres): \n".format(longueur))     #on demande à l'utilisateur un mot de la longueur du mot à trouver
    PROP=list(propo)                        #on transforme la proposition en liste

    if len(PROP)!=longueur:                #on vérifie que le mot proposé est de la bonne couleur
        print("Pas bonne longueur")        #on renvoie un message d'erreur si la longueur ne correspond pas
        prop(MOT,longueur)                 #on demande une nouvelle proposition au joueur
        return 0
    malplacees=[]                           #on créer une liste pour signaler les lettres mal placées
    fausses=[]                              #on créer une liste pour signaler les lettres fausses
    tempo=cp.deepcopy(MOT)                  #on effectue une copie profonde de la liste contenant le mot
    indexaenlever=[]
    
    for i in range(len(PROP)): #test des bonnes lettres bien placées
        if PROP[i]==MOT[i]:                 #on compare la i-ème lettre du mot à trouvé avec la i-ème lettre du mot proposé
            bonnes[i]=PROP[i]               #si elles sont égales, on l'enregistre dans la liste des lettres trouvées
            indexaenlever.append(i)
                        
            
            
    if len(indexaenlever)==0:                   #enleve les bonnes lettres du mot temporaire
        pass
    else:
        #print(indexaenlever)
        for k in range(1,len(indexaenlever)+1):
            a=indexaenlever[-k]
            print(a,tempo)
            del tempo[a]
            del PROP[a]

    if len(PROP)==0:
        #print("TU AS GAGNE")
        return 0

    def malp(malplacees,fausses,PROP,MOT,tempo):

        #print("tempo : ",tempo)
        #print("PROP : ",PROP)
        
        if len(PROP)==0:
            return 0
        if PROP[0] in tempo:
            malplacees.append(PROP[0])

            I=tempo.index(PROP[0])
            del tempo[I]
            
            del PROP[0]
        else:
            fausses.append(PROP[0])
            del PROP[0]
        malp(malplacees,fausses,PROP,MOT,tempo)
    malp(malplacees,fausses,PROP,MOT,tempo)
    
    global nb_essais
    nb_essais+=1
    print("Bonnes : ",bonnes)               #on indique au joueur les lettres bien placées
    print("Mal Placées : ",malplacees)      #les lettres mal placées
    print("Fausses : ",fausses)             #les lettres qui n'appartiennet pas au mot à trouver

    prop(MOT,longueur)

prop(MOT,longueur)
        
            
            
    

    
            
            
    
