import re
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from sutom import *
import sqlite3


app=Flask(__name__)

global ini #initialisation d'une variable ini qui va permettre de savoir si on est au début d'un jeu ou non
ini =0

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
    global ini,L,bonnes
    if ini==0:
        ini+=1
        L=[]
        g=""
        motatrouve="plage" # A LIER AVEC LA BD
        longueuratrouve=len(motatrouve)
        bonnes = ['-' for i in range(longueuratrouve)] 
        return render_template('jeusanslogin.html',liste=L)
    else:
        motatrouve="plage" # A LIER AVEC LA BD
        longueuratrouve=len(motatrouve)
        g=""
        mot=request.form.get("motprop")
        if mot == "" or len(mot)!=longueuratrouve:
            pass      # empecher de faire des mots nuls ou meme de mauvaises longueurs

        bonnes,bonnesponctuel,malponctuel,faussesponctuel=prop(mot,motatrouve,longueuratrouve,bonnes)
        #print(bonnes)
        
        if bonnes==0:
            g="Vous avez gagné ! "
            L.append("{}".format(mot))
        else:
            L.append("{}, {}, {}, {}, {}".format(mot,bonnes,bonnesponctuel,malponctuel,faussesponctuel))
        return render_template('jeusanslogin.html',liste=L,gagne=g)

    

@app.route('/jeulogin')
def jeulogin():
    return render_template('jeulogin.html')

@app.route('/historique_score')
def historique_score():
    return render_template('historique_score.html')