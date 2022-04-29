import sutom as s

def test_sutom_1():
    res = s.prop("DEUX","DEUX",4,['-','-','-','-'])
    assert res == (0,0,0,0)
    
def test_sutom_2():
    res = s.prop("DEUX","BLEU",4,['-','-','-','-'])
    assert res == (['-','-','-','-'],['-','-','-','-'],['-','E','U','-'],['D','-','-','X'])

def test_sutom_3():
    res = s.prop("APPAREILS","PROTOCOLE",9,['-','-','-','-','-','-','-','-','-'])
    assert res == (['-','-','-','-''-','-','-','L','-'],['-','-','-','-','-','-','-','L','-'],['-','P','-','-','R','E','-','-','-'],['A','-','P','A','-','-','I','-','S'])

def test_sutom_4():
    res = s.prop()
    assert res== ()
    
def test_sutom_5():
    res = s.prop()
    assert res== ()
    
def test_sutom_6():
    res = s.prop()
    assert res== ()