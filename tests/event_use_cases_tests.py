import unittest
from datetime import date
from unittest.mock import MagicMock
from eduschedule_lib.domain.event import Event
from eduschedule_lib.use_cases.event_use_cases import (
    ListEventsUseCase,
    GetEventUseCase,
    CreateEventUseCase,
    UpdateEventUseCase,
    DeleteEventUseCase,
)


class TestEventUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_event_repository = MagicMock()

    def test_list_events_use_case(self):
        events_data = [
            Event(1, "Event 1", "Description 1", date(2024, 3, 21)),
            Event(2, "Event 2", "Description 2", date(2024, 3, 22)),
            Event(3, "Event 3", "Description 3", date(2024, 3, 23)),
        ]
        self.mock_event_repository.list.return_value = events_data
        list_events_use_case = ListEventsUseCase(self.mock_event_repository)
        events = list_events_use_case.execute()
        self.assertEqual(events, events_data)

    def test_get_event_use_case(self):
        event_data = Event(1, "Event 1", "Description 1", date(2024, 3, 21))
        self.mock_event_repository.get.return_value = event_data
        get_event_use_case = GetEventUseCase(self.mock_event_repository)
        event = get_event_use_case.execute(1)
        self.assertEqual(event, event_data)

    def test_create_event_use_case(self):
        event_data = Event(None, "New Event", "New Description", date(2024, 3, 21))
        self.mock_event_repository.create.return_value = 1
        create_event_use_case = CreateEventUseCase(self.mock_event_repository)
        event_id = create_event_use_case.execute(event_data)
        self.assertEqual(event_id, 1)

    def test_update_event_use_case(self):
        event_data = Event(1, "Updated Event", "Updated Description", date(2024, 3, 21))
        self.mock_event_repository.update.return_value = True
        update_event_use_case = UpdateEventUseCase(self.mock_event_repository)
        result = update_event_use_case.execute(event_data)
        self.assertTrue(result)

    def test_delete_event_use_case(self):
        self.mock_event_repository.delete.return_value = True
        delete_event_use_case = DeleteEventUseCase(self.mock_event_repository)
        result = delete_event_use_case.execute(1)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
