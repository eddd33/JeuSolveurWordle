import copy as cp

def transformation(L,bonnes,mal,fausses,bonnesponctuel,malponctuel,faussesponctuel):
    T=[]
    bonnes=singularite(bonnes)
    mal=singularite(mal)
    fausses=singularite(fausses)

    #si les lettres bonnes sont au bonne endroit

    if len(bonnes)!=0:
        for mot in L:
            longb=len(bonnes)
            compte=0
            for b in bonnes:
                if mot[b[1]]==b[0]:
                    compte+=1
            if compte==longb:
                T.append(mot)
    else:
        for mot in L:
            T.append(mot)
                    

    
    #si parmis ces mots il n'y a pas une des lettres mal placés, on les enlève
    T2=cp.deepcopy(T)
    for mot in T2:
        for m in mal:
            if not m[0] in mot:
                T.remove(mot)
                break
    T2=cp.deepcopy(T)
    for mot in T2:
        for m in mal:
            if mot[m[1]]==m[0]:
                T.remove(mot)
                break

    # ubuf=[]                                         #liste contenant les lettres qui sont dans bonnes (ou mal) et aussi fausses
    # for f in fausses:
    #     for b in bonnes:
    #         if f==b[0] and not f in ubuf:
    #             ubuf.append(f)
    #     fsingularite(L)or m in mal:
    #         if f==m[0] and not f in ubuf:
    #             ubuf.append(f)

    #                                      #compt de lettres bonnes ou mal placees  où une occurence de cette lettre est fausse
    # for u in ubuf:
    #     compt=0
    #     for b in bonnes:
    #         if b[0]==u:
    #             compt+=1
    #     for m in malponctuel:
    #         if m[0]==u:
    #             compt+=1
    #     print(compt)  
    #     for mot in T:
    #         c=0
    #         for lettre in mot:
    #             if lettre == u:
    #                 c+=1
    #         if c>compt:
    #             T.remove(mot)
    #             break
    # print(ubuf)




    aenlever=[]
    
    for f in fausses:                   #les deux prochaines boucles for sont pour enlever les fausses lettres (les vraies)
        #print("f",f)
        k=0
        a=0
        for b in bonnes:
            if f==b[0]:
                k+=1
        if k==0 and f not in aenlever:
            a+=1
        k=0
        for m in mal:
            if f==m[0]:
                k+=1
        if k==0 and f not in aenlever:
            a+=1
        #print("a",a)
        if a==2:
            aenlever.append(f)
    #print("aenleve",aenlever)
    #print("T1",T)
    T2=cp.deepcopy(T)
    for mot in T2:
        #print(mot)
        for lettre in mot:
            if lettre in aenlever:
                #print(mot)
                T.remove(mot)
                break

    


    for f in faussesponctuel:       #enleve les mots avec une lettre bonne et une lettre fausses communes
        c=0
        for b in bonnesponctuel:  #compte le nombre d'occurence de la fausse lettre dans les lettres bonnes du mot proposé
            if b[0]==f:
                c+=1
        for m in malponctuel:     #compte le nombre d'occurence de la fausse lettre dans les lettres bonnes du mot proposé
            if m[0]==f:
                c+=1
        T2=cp.deepcopy(T)
        for mot in T2:
            if occurence(mot,f)>c:
                #print("ca enleve des trucs")
                T.remove(mot)
                
                

    #print(bonnes,mal,malponctuel,fausses)
    #print("T",T)          

    return T

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

def occurence(mot,lettre):
    c=0
    for l in mot:
        if l==lettre:
            c+=1
    return c