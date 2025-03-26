class Arbitre:
    def __init__(self, id_arbitre: int, nom: str, prenom: str, id_nationalite: int):
        self.id_arbitre = id_arbitre
        self.nom = nom
        self.prenom = prenom
        self.id_nationalite = id_nationalite

    def to_dict(self):
        return {
            "id_arbitre": self.id_arbitre,
            "nom": self.nom,
            "prenom": self.prenom,
            "id_nationalite": self.id_nationalite
        }
