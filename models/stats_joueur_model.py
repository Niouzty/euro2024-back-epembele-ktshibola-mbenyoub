class StatsJoueur:
    def __init__(self, id_stats: int, id_joueur: int, id_rencontre: int, buts: int, passes: int, cartons_jaunes: int, cartons_rouges: int):
        self.id_stats = id_stats
        self.id_joueur = id_joueur
        self.id_rencontre = id_rencontre
        self.buts = buts
        self.passes = passes
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def to_dict(self):
        return {
            "id_stats": self.id_stats,
            "id_joueur": self.id_joueur,
            "id_rencontre": self.id_rencontre,
            "buts": self.buts,
            "passes": self.passes,
            "cartons_jaunes": self.cartons_jaunes,
            "cartons_rouges": self.cartons_rouges
        }

    def __lt__(self, other):
        return self.buts < other.buts