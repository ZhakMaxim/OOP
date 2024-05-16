from enum import Enum
from dataclasses import dataclass
class UserStatus(Enum):
    STUDENT = 'ученик'
    TEACHER = 'учитель'
    ADMINISTRATION = 'администрация'


@dataclass(frozen=True)
class User:
    _id: int
    _login: str
    _password: str
    _status: UserStatus
    _student_id: int = None

    @property
    def id(self):
        return self._id

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def status(self):
        return self._status

    @property
    def student_id(self):
        return self._student_id

