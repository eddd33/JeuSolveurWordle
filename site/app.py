import re
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import sqlite3


app=Flask(__name__)


def testconnect():
    global login
    if 'login' in globals() :
        return True
    else:
        return False

@app.route('/')
def initial():
    return render_template('prelayout.html')

@app.route('/inscription',methods=["GET","POST"])
def inscription():
    return render_template('inscription.html')

@app.route('/login')
def connexion():
    return render_template('login.html')

@app.route('/jeusanslogin')
def jeusanslogin():
    return render_template('jeusanslogin.html')

@app.route('/jeulogin')
def jeulogin():
    return render_template('jeulogin.html')

@app.route('/historique_score')
def historique_score():
    return render_template('historique_score.html')