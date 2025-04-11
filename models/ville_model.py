
class Ville:
    def __init__(self, id_ville: int, nom: str):
        self.id_ville = id_ville
        self.nom = nom

    def to_dict(self):
        return {
            "id_ville": self.id_ville,
            "nom": self.nom,
        }

    def __lt__(self, other):
        return self.nom < other.nom