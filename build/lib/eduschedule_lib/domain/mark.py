from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Mark:
    _id: int
    _value: int
    _date: date
    _subject: str
    _student_id: int

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @property
    def date(self):
        return self._date

    @property
    def subject(self):
        return self._subject

    @property
    def student_id(self):
        return self._student_id


