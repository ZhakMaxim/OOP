import unittest
from datetime import date
from unittest.mock import MagicMock
from eduschedule_lib.domain.mark import Mark
from eduschedule_lib.use_cases.mark_use_cases import (
    CreateMarkUseCase,
    GetMarkUseCase,
    UpdateMarkUseCase,
    DeleteMarkUseCase,
)


class TestMarkUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_mark_repository = MagicMock()

    def test_create_mark_use_case(self):
        mark_data = Mark(None, 90, date(2024, 3, 21), 1)
        self.mock_mark_repository.create.return_value = 1
        create_mark_use_case = CreateMarkUseCase(self.mock_mark_repository)
        mark_id = create_mark_use_case.execute(mark_data, 1)
        self.assertEqual(mark_id, 1)

    def test_get_mark_use_case(self):
        mark_data = Mark(1, 90, date(2024, 3, 21), 1)
        self.mock_mark_repository.get.return_value = mark_data
        get_mark_use_case = GetMarkUseCase(self.mock_mark_repository)
        mark = get_mark_use_case.execute(1)
        self.assertEqual(mark, mark_data)

    def test_update_mark_use_case(self):
        mark_data = Mark(1, 95, date(2024, 3, 21), 1)
        self.mock_mark_repository.update.return_value = True
        update_mark_use_case = UpdateMarkUseCase(self.mock_mark_repository)
        result = update_mark_use_case.execute(mark_data)
        self.assertTrue(result)

    def test_delete_mark_use_case(self):
        self.mock_mark_repository.delete.return_value = True
        delete_mark_use_case = DeleteMarkUseCase(self.mock_mark_repository)
        result = delete_mark_use_case.execute(1)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
