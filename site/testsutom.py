import sutom as s

def test_sutom_1():
    res = s.prop("deux","deux",4,['-','-','-','-'])
    assert res == (0,0,0,0)
    
def test_sutom_2():
    res = s.prop("deux","bleu",4,['-','-','-','-'])
    assert res == (['-','-','-','-'],['-','-','-','-'],['-','e','u','-'],['d','-','-','x'])

def test_sutom_3():
    res = s.prop("appareils","protocole",9,['-','-','-','-','-','-','-','-','-'])
    assert res == (['-','-','-','-','-','-','-','l','-'],['-','-','-','-','-','-','-','l','-'],['-','p','-','-','r','e','-','-','-'],['a','-','p','a','-','-','i','-','s'])

def test_sutom_4():
    res = s.prop("plage","minou",5,['-','-','-','-','-'])
    assert res== (['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['p','l','a','g','e'])
    
def test_sutom_5():
    res = s.prop("plage","minou",5,['m','i','-','o','-'])
    assert res== (['m','i','-','o','-'],['-','-','-','-','-'],['-','-','-','-','-'],['p','l','a','g','e'])
"""
def test_sutom_6():
    res = s.prop()
    assert res== ()  """

