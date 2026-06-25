import sqlite3
from datetime import datetime

NOM_FICHIER = "tournoi.db"


def initialiser():
    connexion = sqlite3.connect(NOM_FICHIER)
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS historique (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gagnant TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS equipe_preferee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipe TEXT NOT NULL
        )
    """)
    connexion.commit()
    connexion.close()


def enregistrer_resultat(gagnant):
    connexion = sqlite3.connect(NOM_FICHIER)
    connexion.execute(
        "INSERT INTO historique (gagnant, date) VALUES (?, ?)",
        (gagnant, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    connexion.commit()
    connexion.close()


def recuperer_historique():
    connexion = sqlite3.connect(NOM_FICHIER)
    curseur = connexion.execute("SELECT gagnant, date FROM historique ORDER BY id DESC")
    resultats = curseur.fetchall()
    connexion.close()
    return [{"gagnant": ligne[0], "date": ligne[1]} for ligne in resultats]


def clear_historique():
    connexion = sqlite3.connect(NOM_FICHIER)
    connexion.execute("DELETE FROM historique")
    connexion.commit()
    connexion.close()


def clear_keep_france():
    connexion = sqlite3.connect(NOM_FICHIER)
    connexion.execute("DELETE FROM historique WHERE gagnant IS NOT 'France'")
    connexion.commit()
    connexion.close()

def sauvegarder_equipe_preferee(equipe):
    conn = sqlite3.connect("tournoi.db")
    c = conn.cursor()
    c.execute("INSERT INTO equipe_preferee (equipe) VALUES (?)", (equipe,))
    conn.commit()
    conn.close()

def recuperer_equipe_preferee():
    conn = sqlite3.connect("tournoi.db")
    c = conn.cursor()
    c.execute("SELECT equipe FROM equipe_preferee ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result[0] if result else None