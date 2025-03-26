class Equipe:
    def __init__(self, id_equipe: int, nom: str, ville: str):
        self.id_equipe = id_equipe
        self.nom = nom
        self.ville = ville

    def to_dict(self):
        return {
            "id_equipe": self.id_equipe,
            "nom": self.nom,
            "ville": self.ville
        }

    def __lt__(self, other):
        return self.nom < other.nom