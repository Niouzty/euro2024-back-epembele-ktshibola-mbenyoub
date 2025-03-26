
class Ville:
    def __init__(self, id_ville: int, nom: str, pays: str):
        self.id_ville = id_ville
        self.nom = nom
        self.pays = pays

    def to_dict(self):
        return {
            "id_ville": self.id_ville,
            "nom": self.nom,
            "pays": self.pays
        }

    def __lt__(self, other):
        return self.nom < other.nom