from eduschedule.repositores.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user):
        return self.user_repository.create(user)