import unittest
from unittest.mock import MagicMock
from eduschedule_lib.domain.lesson import Lesson
from eduschedule_lib.use_cases.lesson_use_cases import (
    CreateLessonRepository,
    GetLessonUseCase,
    UpdateLessonUseCase,
    DeleteLessonUseCase,
)


class TestLessonUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_lesson_repository = MagicMock()
        self.mock_schedule_repository = MagicMock()

    def test_create_lesson_use_case(self):
        lesson_data = Lesson(None, "Math", "Monday", "09:00", "10:00", "Room 101", 1)
        self.mock_lesson_repository.create.return_value = 1
        create_lesson_use_case = CreateLessonRepository(self.mock_lesson_repository)
        lesson_id = create_lesson_use_case.execute(lesson_data, 1)
        self.assertEqual(lesson_id, 1)

    def test_get_lesson_use_case(self):
        lesson_data = Lesson(1, "Math", "Monday", "09:00", "10:00", "Room 101", 1)
        self.mock_lesson_repository.get.return_value = lesson_data
        get_lesson_use_case = GetLessonUseCase(self.mock_lesson_repository)
        lesson = get_lesson_use_case.execute(1, 1)
        self.assertEqual(lesson, lesson_data)

    def test_update_lesson_use_case(self):
        lesson_data = Lesson(1, "Updated Math", "Tuesday", "10:00", "11:00", "Room 102", 1)
        self.mock_lesson_repository.update.return_value = True
        update_lesson_use_case = UpdateLessonUseCase(self.mock_lesson_repository)
        result = update_lesson_use_case.execute(lesson_data)
        self.assertTrue(result)

    def test_delete_lesson_use_case(self):
        self.mock_lesson_repository.delete.return_value = True
        delete_lesson_use_case = DeleteLessonUseCase(self.mock_lesson_repository)
        result = delete_lesson_use_case.execute(1, 1)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
