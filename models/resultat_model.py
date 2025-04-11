class Resultat:
    def __init__(self, id_resultat: int, buts_equipe1_temps_reglementaire: int, buts_equipe2_temps_reglementaire: int,
                 prolongation: bool = False, tirs_au_but: bool = False, buts_equipe1_apres_prolongation: int = 0,
                 buts_equipe2_apres_prolongation: int = 0, score_equipe1: int | None = None,
                 score_equipe2: int | None = None, score_tirs_au_but_equipe1: int = 0,
                 score_tirs_au_but_equipe2: int = 0):
        self.id_resultat = id_resultat
        self.buts_equipe1_temps_reglementaire = buts_equipe1_temps_reglementaire
        self.buts_equipe2_temps_reglementaire = buts_equipe2_temps_reglementaire
        self.prolongation = prolongation
        self.tirs_au_but = tirs_au_but
        self.buts_equipe1_apres_prolongation = buts_equipe1_apres_prolongation
        self.buts_equipe2_apres_prolongation = buts_equipe2_apres_prolongation
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2
        self.score_tirs_au_but_equipe1 = score_tirs_au_but_equipe1
        self.score_tirs_au_but_equipe2 = score_tirs_au_but_equipe2

    def to_dict(self):
        return {
            "id_resultat": self.id_resultat,
            "buts_equipe1_temps_reglementaire": self.buts_equipe1_temps_reglementaire,
            "buts_equipe2_temps_reglementaire": self.buts_equipe2_temps_reglementaire,
            "prolongation": self.prolongation,
            "tirs_au_but": self.tirs_au_but,
            "buts_equipe1_apres_prolongation": self.buts_equipe1_apres_prolongation,
            "buts_equipe2_apres_prolongation": self.buts_equipe2_apres_prolongation,
            "score_tirs_au_but_equipe1": self.score_tirs_au_but_equipe1,
            "score_tirs_au_but_equipe2": self.score_tirs_au_but_equipe2
        }

    def __lt__(self, other):
        return (self.score_equipe1 + self.score_equipe2) < (other.score_equipe1 + other.score_equipe2)
