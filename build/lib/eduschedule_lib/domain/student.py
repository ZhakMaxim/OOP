from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    _id: int
    _name: str
    _group_id: int

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def group_id(self):
        return self._group_id

