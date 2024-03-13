from eduschedule.repositores.mark_repository import MarkRepository

class CreateMarkUseCase:
    def __init__(self, mark_repository: MarkRepository):
        self.mark_repository = mark_repository

    def execute(self, mark, student_id):
        mark_id = self.mark_repository.create(mark, student_id=student_id)
        return mark_id

class GetMarkUseCase:
    def __init__(self, mark_repository: MarkRepository):
        self.mark_repository = mark_repository

    def execute(self, mark_id):
        mark = self.mark_repository.get(mark_id)
        return mark

class UpdateMarkUseCase:
    def __init__(self, mark_repository: MarkRepository):
        self.mark_repository = mark_repository

    def execute(self, mark):
        result = self.mark_repository.update(mark)
        return result

class DeleteMarkUseCase:
    def __init__(self, mark_repository: MarkRepository):
        self.mark_repository = mark_repository

    def execute(self, mark_id):
        result = self.mark_repository.delete(mark_id)
        return result
