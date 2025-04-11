import datetime


class Temps:
    def __init__(self, id_temps: int, date_heure_match: datetime.datetime):
        self.id_temps = id_temps
        self.date_heure_match = date_heure_match

    def to_dict(self):
        return {
            "id_temps": self.id_temps,
            "date_heure_match": self.date_heure_match
        }

