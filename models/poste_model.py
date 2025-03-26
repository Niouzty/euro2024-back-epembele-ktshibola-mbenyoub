

class Poste:
    def __init__(self, id_poste: int, nom: str):
        self.id_poste = id_poste
        self.nom = nom

    def to_dict(self):
        return {
            "id_poste": self.id_poste,
            "nom": self.nom
        }

    def __lt__(self, other):
        return self.nom < other.nom