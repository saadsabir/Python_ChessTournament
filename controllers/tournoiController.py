from models.tournoi import Tournoi
import json
import os
import io
from datetime import datetime
PATH = "data/tournaments/"


class tournoiController:
    def __init__(self):
        self
    """
    Function to validate date with format jj/mm/aaaa
    """
    def validate(date_text):
        try:
            if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime("%d/%m/%Y"):
                raise ValueError
            return True
        except ValueError:
            return False
    """
    Ajouter un tournoi
    """
    def add_tournoi(self, nom, lieu, date_debut, remarque):
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(lieu)) < 3:
                return "Le lieu du tournoi doit contenir au minimum trois caractères."
            if len(str(date_debut)) != 10 and not tournoiController.validate(date_debut):
                return "La date de debut du tournoi doit avoir le format jj/mm/aaaa."
            if len(str(remarque)) < 3:
                return "la remarque du tournoi doit contenir au minimum trois caractères."
            Tournois = Tournoi(nom, lieu, date_debut, remarque)
            data = []
            F = PATH+"{}.json".format(nom)
            if os.path.isfile(F):
                with open(F, "r+") as jsonfile:
                    try:
                        data = json.load(jsonfile)
                        if data[0]["nom"] == nom:
                            return 'Ce tournoi existe déja'
                    except ValueError:
                        json.dump(data, jsonfile)
            else:
                with io.open(os.path.join(F), 'w') as jsonfile:
                    jsonfile.write(json.dumps(data, indent=4))
            new_data = Tournois.__dict__
            data.append(new_data)
            with open(F, "w") as jsonfile:
                json.dump(data, jsonfile)
            return "Le tournoi a été ajouté avec succès"
        except Exception as e:
            return e
    """
    Retourner tous les tournois
    """
    def get_tournois(self, dossier):
        try:
            listtournoi = []
            for fichier in os.listdir(dossier):
                if fichier.endswith(".json"):
                    path = os.path.join(dossier, fichier)
                    with open(path) as f:
                        data = json.load(f)
                        listtournoi.extend(data)
            return listtournoi
        except Exception as e:
            return e
    """
    Retourner le nom et la date du tournoi
    """
    def get_nom_date_tournoi(self, nom):
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            new_data = []
            a = PATH + nom + '.json'
            with open(a, 'r')as f:
                data = json.load(f)
            new_data.append(data[0]['nom_tournoi'])
            new_data.append(data[0]['date_debut'])
            new_data.append(data[0]['date_fin'])
            return new_data
        except Exception as e:
            return e

    """
    Retourner un tournoi
    """

    def get_tournoi(self, nom):
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            a = PATH + nom + '.json'
            with open(a, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            return e