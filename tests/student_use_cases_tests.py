import unittest
from unittest.mock import MagicMock
from eduschedule_lib.domain.student import Student
from eduschedule_lib.use_cases.student_use_cases import (
    CreateStudentUseCase,
    GetStudentUseCase,
    UpdateStudentUseCase,
    DeleteStudentUseCase,
)


class TestStudentUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_student_repository = MagicMock()

    def test_create_student_use_case(self):
        student_data = Student(None, "John Doe", 1)
        self.mock_student_repository.create.return_value = 1
        create_student_use_case = CreateStudentUseCase(self.mock_student_repository)
        student_id = create_student_use_case.execute(student_data)
        self.assertEqual(student_id, 1)

    def test_get_student_use_case(self):
        student_data = Student(1, "John Doe", 1)
        self.mock_student_repository.get.return_value = (student_data, [])
        get_student_use_case = GetStudentUseCase(self.mock_student_repository)
        student_info = get_student_use_case.execute(1)
        self.assertEqual(student_info[0], student_data)

    def test_update_student_use_case(self):
        student_data = Student(1, "Jane Doe", 1)
        self.mock_student_repository.update.return_value = True
        update_student_use_case = UpdateStudentUseCase(self.mock_student_repository)
        result = update_student_use_case.execute(student_data)
        self.assertTrue(result)

    def test_delete_student_use_case(self):
        self.mock_student_repository.delete.return_value = True
        delete_student_use_case = DeleteStudentUseCase(self.mock_student_repository)
        result = delete_student_use_case.execute(1)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
