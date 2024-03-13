from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Event():

    _id: int
    _name: str
    _description: str
    _date: date

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def date(self):
        return self._date