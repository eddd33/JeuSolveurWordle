import copy as cp

mot=input("Rentrer le mot a trouver : \n")

MOT = list(mot)
longueur=len(MOT)
print(MOT)
global bonnes
bonnes = ['-' for i in range(longueur)]
def prop(MOT,longueur):
    global bonnes
    propo=input("Proposition ({} lettres): \n".format(longueur))
    PROP=list(propo)

    if len(PROP)!=longueur:
        print("Pas bonne longueur")
        prop(MOT,longueur)
        return 0
    malplacees=[]
    fausses=[]
    tempo=cp.deepcopy(MOT)
    indexaenlever=[]
    
    for i in range(len(PROP)): #test des bonnes lettres bien placées
        if PROP[i]==MOT[i]:
            bonnes[i]=PROP[i]
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

    print("Bonnes : ",bonnes)
    print("Mal Placées : ",malplacees)
    print("Fausses : ",fausses)

    prop(MOT,longueur)

prop(MOT,longueur)
        
            
            
    

    
            
            
    
