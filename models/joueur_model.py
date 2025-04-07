from datetime import date
class Joueur:
    def __init__(self, id_joueur: int, nom: str, prenom: str, date_naissance: date, id_nationalite: int, id_poste: int, num_maillot: int, id_equipe: int, id_stats_joueur: int | None = None):
        self.id_joueur = id_joueur
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_nationalite = id_nationalite
        self.id_poste = id_poste
        self.num_maillot = num_maillot
        self.id_equipe = id_equipe
        self.id_stats_joueur = id_stats_joueur

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.date_naissance.year - ((today.month, today.day) < (self.date_naissance.month, self.date_naissance.day))

    def to_dict(self):
        return {
            "id_joueur": self.id_joueur,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance.isoformat(),
            "age": self.age,
            "id_nationalite": self.id_nationalite,
            "id_poste": self.id_poste,
            "num_maillot": self.num_maillot,
            "id_equipe": self.id_equipe,
            "id_stats_joueur": self.id_stats_joueur
        }

    def __lt__(self, other):
        return self.date_naissance < other.date_naissance
