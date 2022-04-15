import re
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
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

@app.route('/inscription',methods=["GET","POST"])
def inscription():
    return render_template('inscription.html')

@app.route('/login')
def connexion():
    return render_template('login.html')

@app.route('/deconnexion')
def deconnexion():
    return redirect('/accueil')

@app.route('/jeusanslogin',methods=["POST","GET"])
def jeusanslogin():
    global ini,L,bonnes,longueur,essais,nb_essais,verifreload
    print("ini",ini)
    if verifreload!=0:
        ini=0
        verifreload=0
    if ini==0:
        ini+=1
        nb_essais=0
        L=[]
        L.append("Longueur du mot à trouver : {}".format(longueur))
        g=""
        motatrouve="plage" # A LIER AVEC LA BD
        bonnes = ['-' for i in range(longueur)] 
        return render_template('jeusanslogin.html',liste=L)
    else:
        motatrouve="plage" # A LIER AVEC LA BD
        
        g=""
        mot=request.form.get("motprop")
        if mot == "" or len(mot)!=longueur:
            pass      # empecher de faire des mots nuls ou meme de mauvaises longueurs
        
        bonnes,bonnesponctuel,malponctuel,faussesponctuel=prop(mot,motatrouve,longueur,bonnes)
        #print(bonnes)
        nb_essais+=1
        L.pop()
        if bonnes==0:
            g="Vous avez gagné ! "
            verifreload=1
            L.append("{}".format(mot))
        else:
            L.append("{}, {}, {}, {}, {}".format(mot,bonnes,bonnesponctuel,malponctuel,faussesponctuel))
        L.append("Nombre d'essais : {}".format(nb_essais))
        return render_template('jeusanslogin.html',liste=L,gagne=g)

    

@app.route('/jeulogin')
def jeulogin():
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