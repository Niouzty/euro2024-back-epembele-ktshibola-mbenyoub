class Stade:

    def __init__(self, id_stade: int, nom: str, ville: str, capicite: int):
        self.id_stade = id_stade
        self.nom = nom
        self.ville = ville
        self.capicite = capicite



    def to_dict(self):
        return {
            "id_stade": self.id_stade,
            "nom": self.nom,
            "ville": self.ville,
            "capacite": self.capicite
        }


    def __lt__(self, other):
        return self.capicite < other.capicite


