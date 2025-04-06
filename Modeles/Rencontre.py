from datetime import date

class Rencontre:
    def __init__(self, equipe1: str, equipe2: str, jour: int, mois: int, annee: int):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.date = date(annee, mois, jour)

    
