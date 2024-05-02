from dataclasses import dataclass

@dataclass(frozen=True)
class Group:
    _id: int
    _name: str

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


