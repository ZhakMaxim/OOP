from eduschedule.repositores.student_repository import StudentRepository

class CreateStudentUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def execute(self, student):
        student_id = self.student_repository.create(student)
        return student_id

class GetStudentUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def execute(self, student_id):
        student_info = self.student_repository.get(student_id)
        return student_info

class UpdateStudentUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def execute(self, student):
        success = self.student_repository.update(student)
        return success

class DeleteStudentUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def execute(self, student_id):
        result = self.student_repository.delete(student_id)
        return result
