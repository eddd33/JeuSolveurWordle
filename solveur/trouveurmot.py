from compteuroccurence import *
import copy as cp
def trouveurmot(L,deja=[],lettresfausses=[],nb_essais=0):  #lettres fausses pas utiles
    occurences=compteuroccurenceliste(L)
    #print("occurences",occurences)
    scoremots=[]
    for mot in L:
        s=0
        if mot in deja:  #si le mot est un mot déja proposé, on l'élimine et on continue au prochain mot
            s+=999

        for lettre in mot:
            if lettre in lettresfausses:           # si une des lettres est fausse, on elimine le mot 
                s+=999
            else:
                classement=occurences.index(lettre)  #avec un décalage d'un du au démarrage à 0 des listes
                s+=classement                          # on ajoute le classement de la lettre au score, le but étant d'avoir un score minimal

        if nb_essais<3:
            motliste=list(mot)
            motliste2=cp.deepcopy(motliste)
            motliste2=singularite(motliste2)
            for lettre in motliste:
                if lettre in motliste2:
                    if occurence(mot,lettre)>1:
                        s+=occurence(mot,lettre)*100
                    motliste2.remove(lettre)



        scoremots.append(s)         #comprend la liste des scores des mots dans le meme ordre que L
        
    #print("scoremots",scoremots)
    def donnermot(L,scoremot):
        if len(L)<6:
            print("Mots restants: ",L)
        motàdonner=L[scoremot.index(min(scoremot))]
        indexmot=L.index(motàdonner)
        
        return motàdonner


    return donnermot(L,scoremots)


def occurence(mot,lettre):
    c=0
    for l in mot:
        if l==lettre:
            c+=1
    return c
def singularite(L):
    a=0
    for i in range(len(L)):
        if L[i] in L[:i] or L[i] in L[i+1:]:
            del L[i]
            a=1
            break
    if a==0:
        return L
    else:
        return singularite(L)

#print("resultat",trouveurmot(["azer","abbe","abbe","rase","rare","pare","mrar","eore"]))


