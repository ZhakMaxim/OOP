from dataclasses import dataclass

@dataclass(frozen=True)
class Schedule:
    _id: int
    _group_id: int

    @property
    def id(self):
        return self._id

    @property
    def group_id(self):
        return self._group_id


