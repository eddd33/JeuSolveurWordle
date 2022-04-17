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
essais=6
longueur=5
ini =0
verifreload=0

def testconnect():
    global login
    if 'login' in globals() :
        return True
    else:
        return False

@app.route('/')
def initial():
    return render_template('accueil.html')

@app.route('/accueil')
def accueil():
    global ini
    ini=0
    return render_template('accueil.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/register',method=["POST"])
def register():
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
    cur.execute("INSERT INTO user (pseudo,mdp) VALUES (?,?)",(login,mdp))
    db.commit()
    db.close()
    return render_template('inscription_reussie.html')

@app.route('/login')
def connexion():
    return render_template('login.html')

@app.route('/deconnexion')
def deconnexion():
    return redirect('/accueil')

@app.route('/jeusanslogin',methods=["POST","GET"])
def jeusanslogin():
    global ini,L,bonnes,longueur,essais,nb_essais,verifreload,motatrouve
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
        #motatrouve="plage" # A LIER AVEC LA BD
        bonnes = ['-' for i in range(longueur)] 
        return render_template('jeusanslogin.html',liste=L)
    else:
        #motatrouve="plage" # A LIER AVEC LA BD
        
        g=""
        mot=request.form.get("motprop")
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

    

@app.route('/jeulogin')
def jeulogin():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute("SELECT mot FROM dico WHERE longueur={}".format(longueur))
    mots=cur.fetchall()
    n=random.randint()
    motatrouve=mots[n]
    db.close()
    return render_template('jeulogin.html')

@app.route('/historique_score')
def historique_score():
    return render_template('historique_score.html')

@app.route("/filtrelettres",methods=["POST","GET"])
def filtrelettres():
    global longueur,ini
    ini=0   #reset le jeu
    longueur=int(request.form.get("nbdelettres"))
    return redirect("/jeusanslogin")

@app.route("/filtrechances",methods=["POST","GET"])
def filtrechances():
    global essais,ini
    ini=0
    essais=int(request.form.get("nbdechances"))
    return redirect("/jeusanslogin")