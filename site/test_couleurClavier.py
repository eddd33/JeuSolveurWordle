import sutom as s

def test_couleurClavier_1():
    res = s.couleurClavier("deux","deux",4,['-','-','-','-'])
    assert res == (0,0,0,0)
    
def test_couleurClavier_2():
    res = s.couleurClavier("deux","bleu",4,['-','-','-','-'])
    assert res == (['-','-','-','-'],['-','-','-','-'],['-','e','u','-'],['d','-','-','x'])

def test_couleurClavier_3():
    res = s.couleurClavier("appareils","protocole",9,['-','-','-','-','-','-','-','-','-'])
    assert res == (['-','-','-','-','-','-','-','l','-'],['-','-','-','-','-','-','-','l','-'],['-','p','-','-','r','e','-','-','-'],['a','-','p','a','-','-','i','-','s'])

def test_couleurClavier_4():
    res = s.couleurClavier("plage","minou",5,['-','-','-','-','-'])
    assert res== (['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['p','l','a','g','e'])
    
def test_couleurClavier_5():
    res = s.couleurClavier("plage","minou",5,['m','i','-','o','-'])
    assert res== (['m','i','-','o','-'],['-','-','-','-','-'],['-','-','-','-','-'],['p','l','a','g','e'])