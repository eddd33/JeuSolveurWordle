

f1 = open("lex.txt","r")
f2 = open("lex_modif.txt","w")

liste_e = f1.readlines()
liste_s = []

for i in range(len(liste_e)):
    if liste_e[i] not in liste_s :
        liste_s.append(liste_e[i])
        if " " not in liste_e[i] and "-" not in liste_e[i]:
                f2.write(liste_e[i])
    

print(liste_e[:5])