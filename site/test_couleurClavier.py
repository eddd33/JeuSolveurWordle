import sutom as s

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def test_couleurClavier_1():
    res = s.couleurClavier(alphabet,["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]
    ,['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],"deux")
    assert res == ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]
    
def test_couleurClavier_2():
    res = s.couleurClavier(alphabet,["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]
    ,['-','-','-','-'],['-','e','u','-'],['d','-','-','x'],"deux")
    assert res == ["w","w","w","g","o","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","o","w","w","g","w","w"]

def test_couleurClavier_3():
    res = s.couleurClavier(alphabet,["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]
    ,['-','-','-','-','-','-','-','l','-'],['-','p','-','-','r','e','-','l','-'],['a','-','p','a','-','-','e','-','s'],"appareils")
    assert res == ['g','w','w','w','o','w','w','w','w','w','w','v','w','w','w','o','w','o','g','w','w','w','w','w','w','w']

def test_couleurClavier_4():
    res = s.couleurClavier(alphabet,["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]
    ,['i','-','-','-','-','-','-'],['-','-','-','-','-','-','g'],['-','c','e','b','e','r','-'],"iceberg")
    assert res== ['w','g','g','w','g','w','o','w','v','w','w','w','w','w','w','w','w','g','w','w','w','w','w','w','w','w']
    
def test_couleurClavier_5():
    res = s.couleurClavier(alphabet,['w','g','g','w','g','w','o','w','v','w','w','w','w','w','w','w','w','g','w','w','w','w','w','w','w','w']
    ,['i','n','-','-','-','-','-'],['-','-','a','-','-','-','g'],['-','-','-','c','t','i','f'],"inactif")
    assert res== ['o','g','g','w','g','g','o','w','v','w','w','w','w','v','w','w','w','g','w','g','w','w','w','w','w','w']

def test_couleurClavier_6():
    res = s.couleurClavier(alphabet,['w','g','g','w','g','w','o','w','v','w','w','w','w','w','w','w','w','g','w','w','w','w','w','w','w','w']
    ,['i','n','e','g','a','u','x'],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-'],"inegaux")
    assert res== ['v','g','g','w','v','w','v','w','v','w','w','w','w','v','w','w','w','g','w','w','v','w','w','v','w','w']