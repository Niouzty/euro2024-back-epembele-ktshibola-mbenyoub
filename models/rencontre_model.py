class Rencontre:
    def __init__(self, id_match: int, id_temps: int, id_stade: int, id_equipe1: int, id_equipe2: int, id_arbitre: int,
                 id_phase: int, id_resultat: int | None = None, nb_spectateurs: int | None = None,
                 nb_cartons_jaunes: int | None = None, nb_cartons_rouges: int | None = None):
        self.id_match = id_match
        self.id_temps = id_temps
        self.id_stade = id_stade
        self.id_equipe1 = id_equipe1
        self.id_equipe2 = id_equipe2
        self.id_arbitre = id_arbitre
        self.id_phase = id_phase
        self.id_resultat = id_resultat
        self.nb_spectateurs = nb_spectateurs
        self.nb_cartons_jaunes = nb_cartons_jaunes
        self.nb_cartons_rouges = nb_cartons_rouges

    def to_dict(self):
        return {
            "id_match": self.id_match,
            "id_temps": self.id_temps,
            "id_stade": self.id_stade,
            "id_equipe1": self.id_equipe1,
            "id_equipe2": self.id_equipe2,
            "id_arbitre": self.id_arbitre,
            "id_phase": self.id_phase,
            "id_resultat": self.id_resultat,
            "nb_spectateurs": self.nb_spectateurs,
            "nb_cartons_jaunes": self.nb_cartons_jaunes,
            "nb_cartons_rouges": self.nb_cartons_rouges
        }

    def __lt__(self, other):
        return self.id_temps < other.id_temps
