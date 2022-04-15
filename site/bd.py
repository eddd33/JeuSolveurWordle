import sqlite3

f1 = open("lex_modif.txt","r")

liste = f1.readlines()

jolieliste = []

for i in range(0,len(liste)):
    liste[i] = liste[i].split(',')
liste = liste[1:]
for i in range(len(liste)):
    if len(liste[i][1])>7 :
        liste[i][1] = liste[i][1][2:4]
    else :
        liste[i][1] = liste[i][1][2:3]
    liste[i][1] = int(liste[i][1])
    liste[i][0] = liste[i][0][1:]

for i in range(len(liste)):
    jolieliste.append((liste[i][0],liste[i][1]))

print(liste[:5])
print(liste[104090:])

print(jolieliste[:5])
print(jolieliste[104090:])


def insert_into(jolieliste):
    try :
        conn = sqlite3.connect('projet.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")
        req = "create or replace table dico (mot text PRIMARY KEY, longueur INTEGER NOT NULL)"
        cur.execute(req)
        sql = "INSERT INTO dico (mot,longueur) VALUES (?,?)"
        cur.executemany(sql, jolieliste)
        conn.commit()
        print("Enregistrements insérés avec succès dans la table dico")
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")
    except sqlite3.Error as error:
        print("Erreur lors de l'insertion dans la table dico", error)

insert_into(jolieliste)