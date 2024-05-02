from eduschedule_lib.interfaces.repository import BaseRepository
from eduschedule_lib.domain.user import User


class UserRepository(BaseRepository):
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create(self, user, *args, **kwargs):
        new_user_id = self.next_id
        new_user = User(_id=new_user_id,
                        _login=user.login,
                        _password=user.password,
                        _status=user.status,
                        _student_id=user.student_id)
        self.users[new_user_id] = new_user
        self.next_id += 1
        return new_user_id

    def list(self, *args, **kwargs):
        pass

    def get(self, user_id, *args, **kwargs):
        pass

    def update(self, user):
        pass

    def delete(self, user_id, *args, **kwargs):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
