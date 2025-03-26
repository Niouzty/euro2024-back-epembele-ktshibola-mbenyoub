

class Temps:
    def __init__(self, id_temps: int, minute: int):
        self.id_temps = id_temps
        self.minute = minute

    def to_dict(self):
        return {
            "id_temps": self.id_temps,
            "minute": self.minute
        }

    def __lt__(self, other):
        return self.minute < other.minute