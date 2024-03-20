import unittest
from unittest.mock import MagicMock
from eduschedule.domain.lesson import Lesson
from eduschedule.use_cases.schedule_use_cases import (
    GetScheduleUseCase,
)

class TestScheduleUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_schedule_repository = MagicMock()

    def test_get_schedule_use_case(self):
        schedule_data = {"id": 1, "group_id": 1}
        self.mock_schedule_repository.get.return_value = schedule_data
        get_schedule_use_case = GetScheduleUseCase(self.mock_schedule_repository)
        schedule = get_schedule_use_case.execute(1)
        self.assertEqual(schedule, schedule_data)