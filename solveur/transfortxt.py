f=open("/home/eleve/project2-E13/solveur/mots.txt","r")
g=open("/home/eleve/project2-E13/solveur/motst.txt","w")
c=0
for ligne in f.readlines():
    LIGNE=ligne
    a=0
    #print(ligne)
    for i in range(len(ligne)):
        if  ligne[i]=="â" or ligne[i]=="à" or ligne[i]=="ä" or ligne[i]=='å':
            LIGNE=LIGNE[:i]+"a"+LIGNE[i+1:]
        elif ligne[i]=="é" or ligne[i]=="è" or ligne[i]=="ê" or ligne[i]=="ë" or ligne[i]=="ᵉ":
            LIGNE=LIGNE[:i]+"e"+LIGNE[i+1:]
        elif ligne[i]=="i" or ligne[i]=="î" or ligne[i]=="ï":
            LIGNE=LIGNE[:i]+"i"+LIGNE[i+1:]
        elif ligne[i]=="û" or ligne[i]=="ù" or ligne[i]=="ü":
            LIGNE=LIGNE[:i]+"u"+LIGNE[i+1:]
        elif ligne[i]=="ô" or ligne[i]=="ö" or ligne[i]=="ó" or ligne[i]=="ō" :
            LIGNE=LIGNE[:i]+"a"+LIGNE[i+1:]
        elif ligne[i]=="œ":
            a+=1
        elif ligne[i]=="æ":
            a+=1
        elif ligne[i]=="ç":
            LIGNE=LIGNE[:i]+"c"+LIGNE[i+1:]
        elif ligne[i]=="ñ":
            LIGNE=LIGNE[:i]+"n"+LIGNE[i+1:]
        else:    
            pass   



    if a==0:
        g.write(LIGNE)