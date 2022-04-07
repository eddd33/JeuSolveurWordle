def transformateur(L):
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
            if  ligneliste[i]=="â" or ligneliste[i]=="à" or ligneliste[i]=="ä" or ligneliste[i]=='å':
                ligneliste[i]="a"
            elif ligneliste[i]=="é" or ligneliste[i]=="è" or ligneliste[i]=="ê" or ligneliste[i]=="ë" or ligneliste[i]=="ᵉ":
                ligneliste[i]="e"
            elif ligneliste[i]=="i" or ligneliste[i]=="î" or ligneliste[i]=="ï":
                ligneliste[i]="i"
            elif ligneliste[i]=="û" or ligneliste[i]=="ù" or ligneliste[i]=="ü":
                ligneliste[i]="u"
            elif ligneliste[i]=="ô" or ligneliste[i]=="ö" or ligneliste[i]=="ó" or ligneliste[i]=="ō" :
                ligneliste[i]="o"
            elif ligneliste[i]=="œ":
                ligneliste[i]="oe"
            elif ligneliste[i]=="æ":
                ligneliste[i]="ae"
            elif ligneliste[i]=="ç":
                ligneliste[i]="c"
            elif ligneliste[i]=="ñ":
                ligneliste[i]="n"
            else:    
                pass
    return L