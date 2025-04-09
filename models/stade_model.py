class Stade:

    def __init__(self, id_stade: int, nom: str, id_ville: str, capacite: int):
        self.id_stade = id_stade
        self.nom = nom
        self.id_ville = id_ville
        self.capacite = capacite



    def to_dict(self):
        return {
            "id_stade": self.id_stade,
            "nom": self.nom,
            "id_ville": self.id_ville,
            "capacite": self.capacite
        }



