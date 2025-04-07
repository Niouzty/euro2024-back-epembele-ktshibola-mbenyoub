class Equipe:
    def __init__(self, id_equipe: int, nom: str, id_groupe:int, id_entraineur:int ):
        self.id_equipe = id_equipe
        self.nom = nom
        self.id_groupe = id_groupe
        self.id_entraineur = id_entraineur

    def to_dict(self):
        return {
            "id_equipe": self.id_equipe,
            "nom": self.nom,
            "ville": self.ville,
            "id_groupe": self.id_groupe, 
            "id_entraineur": self.id_entraineur
        }

    def __lt__(self, other):
        return self.nom < other.noma