
def compteuroccurenceliste(L):
    #f=open("/home/eleve/project2-E13/solveur/mots.txt","r")

    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    compteuralpha=[0 for i in range(26)]
    compteur=0
    for ligne in L:
        #print(list(ligne))
        ligneliste=list(ligne)
        del ligneliste[-1]
        #print(ligneliste)
        for i in range(len(ligneliste)):
        
            indexlettre=alphabet.index(ligneliste[i])
            compteuralpha[indexlettre]+=1
        
    #print(compteuralpha)


    bestletter=[]
    for k in range(len(compteuralpha)):
        m=max(compteuralpha)
        indexlettre=compteuralpha.index(m)
        bestletter.append(alphabet[indexlettre])
        del alphabet[indexlettre]
        del compteuralpha[indexlettre]

    #print(bestletter)
    return bestletter
#compteur()

def compteuroccurence():
    f=open("/home/eleve/project2-E13/solveur/motst.txt","r")
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    compteuralpha=[0 for i in range(26)]
    compteur=0
    for ligne in f.readlines() :
        #print(list(ligne))
        ligneliste=list(ligne)
        del ligneliste[-1]
        #print(ligneliste)
        for i in range(len(ligneliste)):
            if  ligneliste[i]=="â" or ligneliste[i]=="à" or ligneliste[i]=="ä" or ligneliste[i]=='å':
                compteuralpha[0]+=1
            elif ligneliste[i]=="é" or ligneliste[i]=="è" or ligneliste[i]=="ê" or ligneliste[i]=="ë" or ligneliste[i]=="ᵉ":
                compteuralpha[4]+=1
            elif ligneliste[i]=="i" or ligneliste[i]=="î" or ligneliste[i]=="ï":
                compteuralpha[8]+=1
            elif ligneliste[i]=="û" or ligneliste[i]=="ù" or ligneliste[i]=="ü":
                compteuralpha[20]+=1
            elif ligneliste[i]=="ô" or ligneliste[i]=="ö" or ligneliste[i]=="ó" or ligneliste[i]=="ō" :
                compteuralpha[14]+=1
            elif ligneliste[i]=="œ":
                compteuralpha[14]+=1
                compteuralpha[4]+=1
            elif ligneliste[i]=="æ":
                compteuralpha[0]+=1
                compteuralpha[4]+=1
            elif ligneliste[i]=="ç":
                compteuralpha[2]+=1
            elif ligneliste[i]=="ñ":
                compteuralpha[13]+=1
            else:    
                indexlettre=alphabet.index(ligneliste[i])
                compteuralpha[indexlettre]+=1
        
    #print(compteuralpha)


    bestletter=[]
    for k in range(len(compteuralpha)):
        m=max(compteuralpha)
        indexlettre=compteuralpha.index(m)
        bestletter.append((alphabet[indexlettre],m))  #on s'en fiche du nombre d'occurence
        del alphabet[indexlettre]
        del compteuralpha[indexlettre]

    #print(bestletter)
    return bestletter