
class Entraineur:
    def __init__(self, id_entraineur: int, nom: str, prenom: str, id_nationalite: int):
        self.id_entraineur = id_entraineur
        self.nom = nom
        self.prenom = prenom
        self.id_nationalite = id_nationalite

    def to_dict(self):
        return {
            "id_entraineur": self.id_entraineur,
            "nom": self.nom,
            "prenom": self.prenom,
            "id_nationalite": self.id_nationalite
        }