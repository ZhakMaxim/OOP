from enum import Enum
from dataclasses import dataclass
class UserStatus(Enum):
    STUDENT = 'ученик'
    TEACHER = 'учитель'
    ADMINISTRATION = 'администрация'


@dataclass()
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

    @status.setter
    def status(self, new_status):
        if isinstance(new_status, str):
            new_status = UserStatus[new_status]
        self._status = new_status

    @property
    def student_id(self):
        return self._student_id

    def __post_init__(self):
        if isinstance(self._status, str):
            self.status = UserStatus(self._status)

    def __dict__(self):
        return {'_id': self.id, '_login': self.login, '_password': self.password,
                '_status': self.status, '_student_id': self.student_id}

