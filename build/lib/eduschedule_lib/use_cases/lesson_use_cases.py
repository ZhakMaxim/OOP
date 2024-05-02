from eduschedule_lib.repositores.lesson_repository import LessonRepository


class CreateLessonRepository:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson, group_id):
        lesson_id = self.lesson_repository.create(lesson, group_id=group_id)
        return lesson_id

class GetLessonUseCase:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson_id, schedule_id):
        lesson = self.lesson_repository.get(lesson_id, schedule_id=schedule_id)
        return lesson

class UpdateLessonUseCase:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson):
        result = self.lesson_repository.update(lesson)
        return result

class DeleteLessonUseCase:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson_id, schedule_id):
        result = self.lesson_repository.delete(lesson_id, schedule_id=schedule_id)
        return result
