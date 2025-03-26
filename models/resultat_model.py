class Resultat:
    def __init__(self, id_resultat: int, id_rencontre: int, score_equipe1: int, score_equipe2: int):
        self.id_resultat = id_resultat
        self.id_rencontre = id_rencontre
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2

    def to_dict(self):
        return {
            "id_resultat": self.id_resultat,
            "id_rencontre": self.id_rencontre,
            "score_equipe1": self.score_equipe1,
            "score_equipe2": self.score_equipe2
        }

    def __lt__(self, other):
        return (self.score_equipe1 + self.score_equipe2) < (other.score_equipe1 + other.score_equipe2)
