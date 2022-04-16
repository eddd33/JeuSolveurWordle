def transformation(L,bonnes,mal,fausses):
    T=[]
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
    for mot in T:
        for m in mal:
            if not m[0] in mot:
                T.remove(mot)
                break
    for mot in T:
        for m in mal:
            if mot[m[1]]==m[0]:
                T.remove(mot)
                break

    ubuf=[]                                         #liste contenant les lettre qui sont dans bonnes (ou mal) et aussi fausses
    for f in fausses:
        for b in bonnes:
            if f==b[0] and not f in ubuf:
                ubuf.append(f)
        for m in mal:
            if f==m[0] and not f in ubuf:
                ubuf.append(f)

                                         #compt de lettres bonnes ou mal placees  où une occurence de cette lettre est fausse
    for u in ubuf:
        compt=0
        for b in bonnes:
            if b[0]==u:
                compt+=1
        for m in mal:
            if m[0]==u:
                compt+=1
            
        for mot in T:
            c=0
            for lettre in mot:
                if lettre == u:
                    c+=1
            if c>compt:
                T.remove(mot)
                break
                    

    return T