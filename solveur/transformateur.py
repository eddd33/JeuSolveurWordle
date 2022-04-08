def transformation(L,bonnes,mal,fausses):
    print(L)
    for mot in L:               #si une lettre fausse est dans le mot
        for f in fausses:
            if f in mot:
                if mot in L:
                    L.remove(mot)
    print(L)

    for mot in L:               #si une lettre mal placees n'est pas dans le mot
        for m in mal:
            if not m[0] in mot:
                if mot in L:
                    L.remove(mot)
    for mot in L:               #si une lettre mal placees est bien placees dans un mot
        for m in mal:
            if mot[m[1]]==m[0]:
                if mot in L:
                    L.remove(mot)
            
    
    for mot in L:               #si une lettre bonne n'est pas dans le mot
        for b in bonnes:
            if not b[0] in mot:
                if mot in L:
                    L.remove(mot)
    
    for mot in L:
        for b in bonnes:
            if mot[b[1]]!=b[0]: #si la lettre bonne n'est pas au bon endroit
                if mot in L:
                    L.remove(mot)
    return L