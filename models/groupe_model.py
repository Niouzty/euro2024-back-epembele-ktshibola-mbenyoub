class Groupe:
    def __init__(self, id_groupe: int, nom: str):
        self.id_groupe = id_groupe
        self.nom = nom

    def to_dict(self):
        return {
            "id_groupe": self.id_groupe,
            "nom": self.nom
        }

    def __lt__(self, other):
        return self.nom < other.nom