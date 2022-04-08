from compteuroccurence import *
def trouveurmot(L,deja=[],lettresfausses=[]):  #prend un liste de mot, une liste de mot déja utilisé et une liste de lettre a ne pas mettre
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

        scoremots.append(s)         #comprend la liste des scores des mots dans le meme ordre que L
        
    #print("scoremots",scoremots)
    def donnermot(L,scoremot):
        motàdonner=L[scoremot.index(min(scoremot))]
        indexmot=L.index(motàdonner)
        
        return motàdonner


    return donnermot(L,scoremots)


#print("resultat",trouveurmot(["azer","abbe","abbe","rase","rare","pare","mrar","eore"]))


