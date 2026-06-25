import random

# Les 64 equipes qualifiees pour la Coupe du Monde 2026 (format elargi)
equipes = [
    "Mexique", "Coree du Sud", "Tchequie", "Afrique du Sud",
    "Suisse", "Canada", "Qatar", "Bosnie-Herzegovine",
    "Bresil", "Maroc", "Ecosse", "Haiti",
    "Etats-Unis", "Turquie", "Australie", "Paraguay",
    "Allemagne", "Equateur", "Cote d'Ivoire", "Curacao",
    "Pays-Bas", "Japon", "Suede", "Tunisie",
    "Belgique", "Iran", "Egypte", "Nouvelle-Zelande",
    "Espagne", "Uruguay", "Arabie Saoudite", "Cap-Vert",
    "France", "Senegal", "Norvege", "Irak",
    "Argentine", "Autriche", "Algerie", "Jordanie",
    "Portugal", "Colombie", "RD Congo", "Ouzbekistan",
    "Angleterre", "Croatie", "Panama", "Ghana",
    "Pologne", "Serbie", "Ukraine", "Roumanie",
    "Nigeria", "Cameroun", "Mali", "Kenya",
    "Chili", "Venezuela", "Bolivie", "Costa Rica",
    "Irak", "Vietnam", "Inde", "Bahrein"
]

# Nombre de coupes du monde gagnees par equipe
coupes_gagnees = {
    "Mexique": 0, "Coree du Sud": 0, "Tchequie": 0, "Afrique du Sud": 0,
    "Suisse": 0, "Canada": 0, "Qatar": 0, "Bosnie-Herzegovine": 0,
    "Bresil": 5, "Maroc": 0, "Ecosse": 0, "Haiti": 0,
    "Etats-Unis": 0, "Turquie": 0, "Australie": 0, "Paraguay": 0,
    "Allemagne": 4, "Equateur": 0, "Cote d'Ivoire": 0, "Curacao": 0,
    "Pays-Bas": 0, "Japon": 0, "Suede": 0, "Tunisie": 0,
    "Belgique": 0, "Iran": 0, "Egypte": 0, "Nouvelle-Zelande": 0,
    "Espagne": 1, "Uruguay": 2, "Arabie Saoudite": 0, "Cap-Vert": 0,
    "France": 2, "Senegal": 0, "Norvege": 0, "Irak": 0,
    "Argentine": 3, "Autriche": 0, "Algerie": 0, "Jordanie": 0,
    "Portugal": 0, "Colombie": 0, "RD Congo": 0, "Ouzbekistan": 0,
    "Angleterre": 1, "Croatie": 0, "Panama": 0, "Ghana": 0,
    # 16 equipes supplementaires
    "Pologne": 0, "Serbie": 0, "Ukraine": 0, "Roumanie": 0,
    "Nigeria": 0, "Cameroun": 0, "Mali": 0, "Kenya": 0,
    "Chili": 0, "Venezuela": 0, "Bolivie": 0, "Costa Rica": 0,
    "Vietnam": 0, "Inde": 0, "Bahrein": 0
}

# Classement FIFA
classement_fifa = {
    "Argentine": 1, "Espagne": 2, "France": 3, "Angleterre": 4,
    "Portugal": 5, "Bresil": 6, "Maroc": 7, "Pays-Bas": 8,
    "Belgique": 9, "Allemagne": 10, "Croatie": 11, "Colombie": 13,
    "Mexique": 14, "Senegal": 15, "Uruguay": 16, "Etats-Unis": 17,
    "Japon": 18, "Suisse": 19, "Iran": 20, "Turquie": 22,
    "Equateur": 23, "Autriche": 24, "Coree du Sud": 25, "Australie": 27,
    "Algerie": 28, "Egypte": 29, "Canada": 30, "Norvege": 31,
    "Cote d'Ivoire": 33, "Panama": 34, "Suede": 38, "Tchequie": 40,
    "Paraguay": 41, "Ecosse": 42, "Tunisie": 45, "RD Congo": 46,
    "Ouzbekistan": 50, "Qatar": 56, "Irak": 57, "Afrique du Sud": 60,
    "Arabie Saoudite": 61, "Jordanie": 63, "Bosnie-Herzegovine": 64,
    "Cap-Vert": 67, "Ghana": 73, "Curacao": 82, "Haiti": 83,
    "Nouvelle-Zelande": 85,
    "Pologne": 24, "Serbie": 33, "Ukraine": 22, "Roumanie": 46,
    "Nigeria": 49, "Cameroun": 52, "Mali": 57, "Kenya": 102,
    "Chili": 55, "Venezuela": 58, "Bolivie": 85, "Costa Rica": 87,
    "Vietnam": 116, "Inde": 126, "Bahrein": 88
}

# Codes drapeaux
drapeaux = {
    "Mexique": "mx", "Coree du Sud": "kr", "Tchequie": "cz", "Afrique du Sud": "za",
    "Suisse": "ch", "Canada": "ca", "Qatar": "qa", "Bosnie-Herzegovine": "ba",
    "Bresil": "br", "Maroc": "ma", "Ecosse": "gb-sct", "Haiti": "ht",
    "Etats-Unis": "us", "Turquie": "tr", "Australie": "au", "Paraguay": "py",
    "Allemagne": "de", "Equateur": "ec", "Cote d'Ivoire": "ci", "Curacao": "cw",
    "Pays-Bas": "nl", "Japon": "jp", "Suede": "se", "Tunisie": "tn",
    "Belgique": "be", "Iran": "ir", "Egypte": "eg", "Nouvelle-Zelande": "nz",
    "Espagne": "es", "Uruguay": "uy", "Arabie Saoudite": "sa", "Cap-Vert": "cv",
    "France": "fr", "Senegal": "sn", "Norvege": "no", "Irak": "iq",
    "Argentine": "ar", "Autriche": "at", "Algerie": "dz", "Jordanie": "jo",
    "Portugal": "pt", "Colombie": "co", "RD Congo": "cd", "Ouzbekistan": "uz",
    "Angleterre": "gb-eng", "Croatie": "hr", "Panama": "pa", "Ghana": "gh",
    "Pologne": "pl", "Serbie": "rs", "Ukraine": "ua", "Roumanie": "ro",
    "Nigeria": "ng", "Cameroun": "cm", "Mali": "ml", "Kenya": "ke",
    "Chili": "cl", "Venezuela": "ve", "Bolivie": "bo", "Costa Rica": "cr",
    "Vietnam": "vn", "Inde": "in", "Bahrein": "bh"
}


def tirer_deux_equipes():
    return random.sample(equipes, 2)


def simuler_match(equipe1, equipe2):
    score1 = random.randint(0, 5)
    score2 = random.randint(0, 5)
    return score1, score2


def afficher_resultat(equipe1, equipe2, score1, score2):
    print(f"{equipe1} {score1} - {score2} {equipe2}")

    if score1 > score2:
        gagnant = equipe1
    elif score2 > score1:
        gagnant = equipe2
    else:
        gagnant = None

    if gagnant:
        print(f"Vainqueur : {gagnant} !")
    else:
        print("Match nul !")


def ajouter_equipe():
    nom = input("Nom de l'equipe a ajouter : ")
    titres = int(input("Nombre de titres : "))
    equipes.append(nom)
    coupes_gagnees[nom] = titres


def afficher_palmares():
    print("\nPalmares (nombre de coupes gagnees) :")
    for equipe, total in coupes_gagnees.items():
        print(f"- {equipe} : {total}")

def simuler_match_pondere(equipe1, equipe2):
    max_rang = max(classement_fifa.values()) + 1
    EXPOSANT = 4.01

    poids1 = (max_rang - classement_fifa.get(equipe1, max_rang)) ** EXPOSANT
    poids2 = (max_rang - classement_fifa.get(equipe2, max_rang)) ** EXPOSANT

    total = poids1 + poids2

    proba1 = poids1 / total * 100
    proba2 = poids2 / total * 100

    print(f"\n{equipe1} (FIFA #{classement_fifa.get(equipe1, '?')} : {proba1:.1f}%) vs {equipe2} (FIFA #{classement_fifa.get(equipe2, '?')} : {proba2:.1f}%)")

    gagnant = random.choices([equipe1, equipe2], weights=[poids1, poids2], k=1)[0]

    if gagnant == equipe1:
        score1 = random.randint(1, 5)
        score2 = random.randint(0, score1 - 1)
    else:
        score2 = random.randint(1, 5)
        score1 = random.randint(0, score2 - 1)

    return score1, score2


def simuler_tournoi():
    print("\nSimulation du tournoi :")

    equipes_en_lice = equipes.copy()
    random.shuffle(equipes_en_lice)
    numero_tour = 1

    while len(equipes_en_lice) > 1:
        qualifies = []
        print(f"\nTour {numero_tour} ({len(equipes_en_lice)} equipes) :")

        i = 0
        while i < len(equipes_en_lice):
            if i + 1 == len(equipes_en_lice):
                # nombre impair d'equipes : la derniere passe directement
                print(f"{equipes_en_lice[i]} qualifie directement (pas d'adversaire)")
                qualifies.append(equipes_en_lice[i])
                i += 1

            equipe1 = equipes_en_lice[i]
            equipe2 = equipes_en_lice[i + 1]

            score1, score2 = simuler_match_pondere(equipe1, equipe2)

            if score1 > score2:
                gagnant_match = equipe1
            elif score2 > score1:
                gagnant_match = equipe2
            else:
                gagnant_match = equipe1

            print(f"{equipe1} {score1} - {score2} {equipe2}  ->  {gagnant_match}")
            qualifies.append(gagnant_match)
            i += 2

        equipes_en_lice = qualifies
        numero_tour += 1

    gagnant = equipes_en_lice[0]
    coupes_gagnees[gagnant] = coupes_gagnees.get(gagnant, 0) + 1

    print("\ngagnant du tournoi : " + gagnant)
    return gagnant


if __name__ == "__main__":
    print("Match du jour de la Coupe du Monde !\n")

    simuler_tournoi()