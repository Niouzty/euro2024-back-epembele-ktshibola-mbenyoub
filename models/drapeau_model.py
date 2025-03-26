class Drapeau:
    def __init__(self, id_drapeau: int, id_equipe: int, chemin_image: str):
        self.id_drapeau = id_drapeau
        self.id_equipe = id_equipe
        self.chemin_image = chemin_image

    def to_dict(self):
        return {
            "id_drapeau": self.id_drapeau,
            "id_equipe": self.id_equipe,
            "chemin_image": self.chemin_image
        }
