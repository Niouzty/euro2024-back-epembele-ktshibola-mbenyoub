class Nationalite:
    def __init__(self, id_nationalite: int, nom: str):
        self.id_nationalite = id_nationalite
        self.nom = nom

    def to_dict(self):
        return {
            "id_nationalite": self.id_nationalite,
            "nom": self.nom
        }

    def __lt__(self, other):
        return self.nom < other.nom