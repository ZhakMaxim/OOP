import unittest
from unittest.mock import MagicMock
from eduschedule_lib.domain.group import Group
from eduschedule_lib.use_cases.group_use_cases import (
    CreateGroupUseCase,
    GetGroupUseCase,
    UpdateGroupUseCase,
    DeleteGroupUseCase,
)


class TestGroupUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_group_repository = MagicMock()

    def test_create_group_use_case(self):
        group_data = Group(None, "New Group")
        self.mock_group_repository.create.return_value = 1
        create_group_use_case = CreateGroupUseCase(self.mock_group_repository)
        group_id = create_group_use_case.execute(group_data)
        self.assertEqual(group_id, 1)

    def test_get_group_use_case(self):
        group_data = Group(1, "Group 1")
        self.mock_group_repository.get.return_value = group_data
        get_group_use_case = GetGroupUseCase(self.mock_group_repository)
        group = get_group_use_case.execute(1)
        self.assertEqual(group, group_data)

    def test_update_group_use_case(self):
        group_data = Group(1, "Updated Group")
        self.mock_group_repository.update.return_value = True
        update_group_use_case = UpdateGroupUseCase(self.mock_group_repository)
        result = update_group_use_case.execute(group_data)
        self.assertTrue(result)

    def test_delete_group_use_case(self):
        self.mock_group_repository.delete.return_value = True
        delete_group_use_case = DeleteGroupUseCase(self.mock_group_repository)
        result = delete_group_use_case.execute(1)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
