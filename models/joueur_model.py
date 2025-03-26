
class Joueur:
    def __init__(self, id_joueur: int, nom: str, prenom: str, age: int, id_equipe: int):
        self.id_joueur = id_joueur
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.id_equipe = id_equipe

    def to_dict(self):
        return {
            "id_joueur": self.id_joueur,
            "nom": self.nom,
            "prenom": self.prenom,
            "age": self.age,
            "id_equipe": self.id_equipe
        }

    def __lt__(self, other):
        return self.age < other.age
