import re
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import random
from sutom import *
import sqlite3


app=Flask(__name__)

global ini #initialisation d'une variable ini qui va permettre de savoir si on est au début d'un jeu ou non
global longueur #longueur du mot
global essais   
global nb_essais #nb d'essais sur la partie en cours
global verifreload # regarde si l'utilisateur a reload apres avoir gagné
global login
login=0
essais=6
longueur=5
ini =0
verifreload=0

def testconnect():
    global login
    if login!=0:
        print(login)
        return True
    else:
        return False

@app.route('/')
def initial():
    global login
    login=0
    return redirect("/accueil")

@app.route('/accueil')
def accueil():
    if testconnect():
        return redirect("/deco")
    global ini
    ini=0
    return render_template('accueil.html')

@app.route('/inscription')
def inscription():
    global login
    login=0
    return render_template('inscription.html')

@app.route('/register',methods=["POST"])
def register():
    global ini
    ini=0
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute("SELECT pseudo FROM user")
    users=cur.fetchall()
    login=request.form.get("login")
    mdp=request.form.get("mdp")
    if not login:
        return render_template('erreur.hmtl',message="Login non renseigné")
    if not mdp:
        return render_template('erreur.hmtl',message="Mot de passe non renseigné")
    if login in users:
        return render_template('erreur.html',message="Login déjà utilisé, veuillez en choisir un autre.")
    cur.execute("INSERT INTO user (pseudo,mdp,parties_jouees,parties_gagnees) VALUES (?,?,0,0)",(login,mdp))
    db.commit()
    db.close()
    return render_template('inscription_reussie.html')

@app.route('/login')
def connexion():
    global ini,login
    ini=0
    login=0
    return render_template('login.html')

@app.route('/loginbis',methods=['POST'])
def loginbis():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    pseudo=request.form.get("login")
    mdp=request.form.get("mdp")
    cur.execute("SELECT pseudo FROM user where pseudo='{}'".format(pseudo))
    users=cur.fetchone()
    print(users)
    
    if not users:
        return render_template('erreur.html',message="Login inconnu. Veuillez vous inscrire.")
    cur.execute("SELECT mdp FROM user WHERE pseudo='{}'".format(pseudo))
    bonmdp=cur.fetchone()[0]
    if mdp!=bonmdp:
        return render_template('erreur.html',message="Mot de passe incorrect")
    global login
    login=pseudo
    return redirect('/jeulogin')

@app.route('/deconnexion')
def deconnexion():
    global login    
    login=0
    return redirect('/accueil')

global mot
mot=0

@app.route('/jeusanslogin',methods=["POST","GET"])
def jeusanslogin():
    if testconnect():
        return redirect("/deco")
    global ini,L,bonnes,longueur,essais,nb_essais,verifreload,motatrouve,mot #j'ai rajouté mot pour pas rajouter un essai quand on refresh
    print("ini",ini)
    
    if verifreload!=0:
        ini=0
        verifreload=0
    if ini==0:
        ini+=1
        nb_essais=0
        L=[]
        L.append("Longueur du mot à trouver : {}".format(longueur))
        db=sqlite3.connect('projet.db')
        cur=db.cursor()
        cur.execute("SELECT mot FROM dico WHERE longueur={}".format(longueur))
        mots=cur.fetchall()
        n=random.randint(0,len(mots))
        motatrouve=mots[n][0]
        print("motatrouve",motatrouve)
        db.close()
        g=""
        bonnes = ['-' for i in range(longueur)] 
        return render_template('jeusanslogin.html',liste=L)
    else:
        
        g=""
        motp=request.form.get("motprop")
        if motp==mot:   #evite les problème de refresh
            pass
        else:
            mot=motp
            print("mot",mot)
            if mot == "" or len(mot)!=longueur:
                L.pop()
                L.append("Mauvaise longueur de mot, réessaye mongolo")      # empecher de faire des mots nuls ou meme de mauvaises longueurs
            else:
                bonnes,bonnesponctuel,malponctuel,faussesponctuel=prop(mot,motatrouve,longueur,bonnes)
                #print(bonnes)
                nb_essais+=1
                L.pop()
                if bonnes==0:
                    g="Vous avez gagné ! "
                    verifreload=1
                    L.append("{}".format(mot))
                elif nb_essais==essais:
                    g="Vous avez perdu ! Le mot était {}".format(motatrouve)
                    verifreload=1
                    L.append("{}, {}, {}, {}, {}".format(mot,bonnes,bonnesponctuel,malponctuel,faussesponctuel))
                else:
                    L.append("{}, {}, {}, {}, {}".format(mot,bonnes,bonnesponctuel,malponctuel,faussesponctuel))
                L.append("Nombre d'essais : {} / {}".format(nb_essais,essais))
       
        return render_template('jeusanslogin.html',liste=L,gagne=g)

    

@app.route('/jeulogin',methods=["GET","POST"])
def jeulogin():
    if not testconnect():
        return redirect('/login')
    global ini,L,bonnes,longueur,essais,nb_essais,verifreload,motatrouve,login
    print("ini",ini)
    
    if verifreload!=0:
        ini=0
        verifreload=0
    if ini==0:
        ini+=1
        nb_essais=0
        L=[]
        L.append("Longueur du mot à trouver : {}".format(longueur))
        db=sqlite3.connect('projet.db')
        cur=db.cursor()
        cur.execute("SELECT mot FROM dico WHERE longueur={}".format(longueur))
        mots=cur.fetchall()
        n=random.randint(0,len(mots))
        motatrouve=mots[n][0]
        print("motatrouve",motatrouve)
        db.close()
        g=""
        
        bonnes = ['-' for i in range(longueur)] 
        return render_template('jeulogin.html',liste=L,login=login)
    else:
        g=""
        print("motprop",request.form.get("motprop"))
        motp=request.form.get("motprop")
        if motp==mot:
            pass
        else:
            if mot == "" or len(mot)!=longueur:
                L.pop()
                L.append("Mauvaise longueur de mot, réessaye mongolo")      # empecher de faire des mots nuls ou meme de mauvaises longueurs
            else:
                bonnes,bonnesponctuel,malponctuel,faussesponctuel=prop(mot,motatrouve,longueur,bonnes)
                #print(bonnes)
                nb_essais+=1
                L.pop()
                if bonnes==0:
                    g="Vous avez gagné ! "
                    verifreload=1
                    L.append("{}".format(mot))
                    db=sqlite3.connect("projet.db")
                    cur=db.cursor()
                    cur.execute("SELECT parties_jouees,parties_gagnees FROM user WHERE pseudo='{}'".format(login))
                    parties=cur.fetchone()
                    part_j,part_g=parties[0]+1,parties[1]+1
                    cur.execute("UPDATE user SET parties_jouees = {} WHERE pseudo = '{}'".format(part_j,login))
                    cur.execute("UPDATE user SET parties_gagnees = {} WHERE pseudo = '{}'".format(part_g,login))

                    db.commit()
                    db.close()
                elif nb_essais==essais:
                    g="Vous avez perdu ! Le mot était {}".format(motatrouve)
                    verifreload=1
                    L.append("{}, {}, {}, {}, {}".format(mot,bonnes,bonnesponctuel,malponctuel,faussesponctuel))
                    db=sqlite3.connect("projet.db")
                    cur=db.cursor()
                    cur.execute("SELECT parties_jouees,parties_gagnees FROM user WHERE pseudo='{}'".format(login))
                    parties=cur.fetchone()
                    part_j,part_g=parties[0]+1,parties[1]
                    cur.execute("UPDATE user SET parties_jouees = {} WHERE pseudo = '{}'".format(part_j,login))

                    db.commit()
                    db.close()
                else:
                    L.append("{}, {}, {}, {}, {}".format(mot,bonnes,bonnesponctuel,malponctuel,faussesponctuel))
                L.append("Nombre d'essais : {} / {}".format(nb_essais,essais))
    return render_template('jeulogin.html',liste=L,gagne=g,login=login)

@app.route('/historique_score')
def historique_score():
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect("projet.db")
    cur=db.cursor()
    cur.execute("SELECT parties_jouees,parties_gagnees FROM user WHERE pseudo={}".format(login))
    parties=cur.fetchall()
    nb_jouees=parties[0]
    nb_gagnees=parties[1]
    return render_template('historique_score.html',login=login,nb_jouees=nb_jouees,nb_gagnees=nb_gagnees)

@app.route("/filtrelettres",methods=["POST","GET"])
def filtrelettres():
    global longueur,ini
    ini=0   #reset le jeu
    longueur=int(request.form.get("nbdelettres"))
    if testconnect():
        return redirect("jeulogin")
    else:
        return redirect("/jeusanslogin")

@app.route("/filtrechances",methods=["POST","GET"])
def filtrechances():
    global essais,ini
    ini=0
    essais=int(request.form.get("nbdechances"))
    if testconnect():
        return redirect("jeulogin")
    else:
        return redirect("/jeusanslogin")

@app.route("/deco")
def deco():
    global login
    login = 0
    return redirect("/accueil")