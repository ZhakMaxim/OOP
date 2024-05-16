class CreateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user):
        return self.user_repository.create(user)

class ListUsersUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.list()


class GetUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id):
        return self.user_repository.get(user_id)


class DeleteUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id):
        return self.user_repository.delete(user_id)


class FindUserByLoginUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, login):
        return self.user_repository.find_by_login(login)

