class CreateMarkUseCase:
    def __init__(self, mark_repository):
        self.mark_repository = mark_repository

    def execute(self, mark):
        mark_id = self.mark_repository.create(mark)
        return mark_id

class GetMarkUseCase:
    def __init__(self, mark_repository):
        self.mark_repository = mark_repository

    def execute(self, mark_id):
        mark = self.mark_repository.get(mark_id)
        return mark

class UpdateMarkUseCase:
    def __init__(self, mark_repository):
        self.mark_repository = mark_repository

    def execute(self, mark):
        result = self.mark_repository.update(mark)
        return result

class DeleteMarkUseCase:
    def __init__(self, mark_repository):
        self.mark_repository = mark_repository

    def execute(self, mark_id):
        result = self.mark_repository.delete(mark_id)
        return result
