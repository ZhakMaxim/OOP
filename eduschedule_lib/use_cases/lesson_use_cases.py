class CreateLessonUseCase:
    def __init__(self, lesson_repository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson, group_id):
        lesson_id = self.lesson_repository.create(lesson, group_id=group_id)
        return lesson_id


class GetLessonUseCase:
    def __init__(self, lesson_repository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson_id):
        lesson = self.lesson_repository.get(lesson_id)
        return lesson


class GetLessonByGroupUseCase:
    def __init__(self, lesson_repository):
        self.lesson_repository = lesson_repository

    def execute(self, group_id):
        result = self.lesson_repository.get_by_group_id(group_id)
        return result


class UpdateLessonUseCase:
    def __init__(self, lesson_repository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson):
        result = self.lesson_repository.update(lesson)
        return result


class DeleteLessonUseCase:
    def __init__(self, lesson_repository):
        self.lesson_repository = lesson_repository

    def execute(self, lesson_id):
        result = self.lesson_repository.delete(lesson_id)
        return result

