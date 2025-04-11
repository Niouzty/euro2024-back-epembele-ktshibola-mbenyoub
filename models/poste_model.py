

class Poste:
    def __init__(self, id_poste: int, nom_poste: str):
        self.id_poste = id_poste
        self.nom_poste = nom_poste

    def to_dict(self):
        return {
            "id_poste": self.id_poste,
            "nom_poste": self.nom_poste
        }

