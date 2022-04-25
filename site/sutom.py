import copy as cp




#bonnes est la liste des lettres à affiché avant de rentrer la prochaine proposition (bonnes lettres globalement sur tous les essais)
#bonnesponctuel est la liste des lettres à afficher à la place de la proposition (bonnes lettres uniquement sur le mot rentré)
#malponctuel est la liste des lettres à afficher à la place de la proposition qui sont mal placées
#faussesponctuel est la liste des lettres à afficher à la place de la proposition qui ne sont pas bonnes.


#mot=input("Rentrer le mot a trouver : \n")    #demande du mot à l'utilisateur

#MOT = list(mot)                             #on transforme le mot en liste de caractères
#longueur=len(MOT)                           #on stock la longueur du mot
#print(MOT)
                             #on stock les lettres trouvées et bien placées dans bonnes
    #on initialise cette liste




def prop(motpropo,MOT,longueur,bonnes):                     #fonction prenant en argument le mot à deviner sous forme de liste de lettre et sa longueur   
    MOT=list(MOT)                                           #on transforme le mot en liste de caractères
    bonnesponctuel = ['-' for i in range(longueur)]         #on (re)initialise les listes 
    malponctuel=['-' for i in range(longueur)]         
    
                                                                    # ligne à remplacer par l'entrée web

    PROP=list(motpropo)                        #on transforme la proposition en liste

    if len(PROP)!=longueur:                #on vérifie que le mot proposé est de la bonne couleur
        print("Pas bonne longueur")        #on renvoie un message d'erreur si la longueur ne correspond pas
        prop(MOT,longueur)                 #on demande une nouvelle proposition au joueur
        return 0
                            
    faussesponctuel=['-' for i in range(longueur)]                             #on créer une liste pour signaler les lettres fausses
    tempo=cp.deepcopy(MOT)                  #on effectue une copie profonde de la liste contenant le mot
    indexaenlever=[]
    
    for i in range(len(PROP)):              #test des bonnes lettres bien placées
        if PROP[i]==MOT[i]:                 #on compare la i-ème lettre du mot à trouvé avec la i-ème lettre du mot proposé
            bonnesponctuel[i]=PROP[i]
            bonnes[i]=PROP[i]               #si elles sont égales, on l'enregistre dans la liste des lettres trouvées
            indexaenlever.append(i)         # indexaenlever va servir pour les doubles lettres (ou +) dans un mot
                        
            
            
    if len(indexaenlever)==0:                   #enleve les bonnes lettres du mot temporaire
        pass
    else:
        #print(indexaenlever)
        for k in range(1,len(indexaenlever)+1):
            a=indexaenlever[-k]
            #print(a,tempo)
            del tempo[a]
            PROP[a]=0

    if len(PROP)==0:
        #print("TU AS GAGNE")
        return 0

    def malp(malponctuel,faussesponctuel,PROP,MOT,tempo,prof):  #fonction testant les lettres bonnes mais mal placées

        #print(PROP,tempo)
        if prof==len(PROP):                 #si la profondeur depasse la longueur du mot
            return 0
        elif PROP[prof]==0:             #si la lettre a déja été traitée
            pass
        elif PROP[prof] in tempo:                    #on regarde si la lettre est dans le mot à trouver
            malponctuel[prof]=PROP[prof]          #on ajoute aux lettres mal placées

            I=tempo.index(PROP[prof])              #on récupère l'index de cette lettre dans le mot à trouver
            del tempo[I]                         # on l'enlève
            PROP[prof]=0                        # on traite la lettre
        else:
            faussesponctuel[prof]=PROP[prof]            #sinon la lettre est fausse
            PROP[prof]=0                                #on traite la lettre
        prof+=1                                 #on augmente la profondeur
        malp(malponctuel,faussesponctuel,PROP,MOT,tempo,prof) #et on le refait jusqu'a ce qu'il n'y ai plus de lettres à tester
    
    malp(malponctuel,faussesponctuel,PROP,MOT,tempo,0)
    
    
    print("Bonnes : ",bonnes)               #on indique au joueur les lettres bien placées
    print("Bonnes sur cette proposition : ",bonnesponctuel)
    print("Mal Placées sur cette proposition : ", malponctuel)              #les lettres qui sont mal placées
    print("Fausses sur cette proposition : ",faussesponctuel)             #les lettres qui n'appartiennet pas au mot à trouver
    #Normalement les 3 listes si dessus se complètent
    
    
    if not '-' in bonnes:
        print("Vous avez gagné")
        return 0,0,0,0

    #prop(MOT,longueur)
    return bonnes,bonnesponctuel,malponctuel,faussesponctuel

    



#def reset():
#    global bonnes
#    bonnes = ['-' for i in range(longueur)]     
#    global nb_essais
#    nb_essais=0
              
            
    

    
            
            
    
