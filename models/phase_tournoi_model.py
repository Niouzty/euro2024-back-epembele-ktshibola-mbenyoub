

class PhaseTournoi:
    def __init__(self, id_phase: int, nom: str):
        self.id_phase = id_phase
        self.nom = nom

    def to_dict(self):
        return {
            "id_phase": self.id_phase,
            "nom": self.nom
        }

    def __lt__(self, other):
        return self.nom < other.nom