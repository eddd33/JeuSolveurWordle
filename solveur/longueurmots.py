
def longueurmots(V):
    f=open("/home/eleve/project2-E13/solveur/mots.txt","r")
    c=0
    longueurs=[[]for i in range(26)]
    for mot in f.readlines():
        #print(mot,len(mot))
        mot=mot[:-1]
        longueurs[len(mot)-1].append(mot)
    

    return longueurs[V-1]

#print(longueurmots(4))