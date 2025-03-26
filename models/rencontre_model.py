

class Rencontre:
    def __init__(self, id_rencontre: int, id_phase: int, date: str, id_stade: int):
        self.id_rencontre = id_rencontre
        self.id_phase = id_phase
        self.date = date
        self.id_stade = id_stade

    def to_dict(self):
        return {
            "id_rencontre": self.id_rencontre,
            "id_phase": self.id_phase,
            "date": self.date,
            "id_stade": self.id_stade
        }

    def __lt__(self, other):
        return self.date < other.date
