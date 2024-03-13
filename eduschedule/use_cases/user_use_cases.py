from eduschedule.repositores.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.student_repository = user_repository

    def execute(self, user):
        self.student_repository.create(user)