import os

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from coupe_du_monde import simuler_tournoi, equipes, coupes_gagnees, drapeaux
import base_donnees as bd

app = Flask(__name__)
CORS(app)

bd.initialiser()

@app.route('/')
def index():
    return render_template('coupe-du-monde.html')

@app.route("/equipes")
def liste_equipes():
    return jsonify([
        {"nom": nom, "drapeau": drapeaux.get(nom, "un"), "titres": coupes_gagnees.get(nom, 0)}
        for nom in equipes
    ])


@app.route("/tournoi")
def tournoi():
    gagnant = simuler_tournoi()
    code_drapeau = drapeaux.get(gagnant, "un")
    bd.enregistrer_resultat(gagnant)
    return jsonify(gagnant=gagnant, drapeau=code_drapeau)


@app.route("/historique")
def historique():
    return jsonify(bd.recuperer_historique())


@app.route("/historique/effacer", methods=["POST"])
def effacer_historique():
    bd.clear_historique()
    return jsonify({"message": "Historique effacé avec succès."})

@app.route("/historique/effacer_sauf_france", methods=["POST"])
def effacer_historique_gagnants_france():
    bd.clear_keep_france()
    return jsonify({"message": "Historique effacé sauf pour la France."})

@app.route('/equipe-preferee')
def equipe_preferee():
    return render_template('equipe-preferee.html')

@app.route("/sauvegarder", methods=["POST"])
def sauvegarder_preferee():
    data = request.get_json()
    bd.sauvegarder_equipe_preferee(data["equipe"])
    return jsonify({"message": "Équipe sauvegardée !"})

@app.route("/recuperer")
def recuperer_equipe_pref():
    return jsonify(bd.recuperer_equipe_preferee)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
