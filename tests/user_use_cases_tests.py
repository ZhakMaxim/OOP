import unittest
from unittest.mock import MagicMock
from eduschedule_lib.domain.user import User, UserStatus
from eduschedule_lib.use_cases.user_use_cases import CreateUserUseCase


class TestUserUseCases(unittest.TestCase):
    def setUp(self):
        self.mock_user_repository = MagicMock()

    def test_create_user_use_case(self):
        user_data = User(None, "user123", "password123", UserStatus.STUDENT, 1)
        self.mock_user_repository.create.return_value = 1
        create_user_use_case = CreateUserUseCase(self.mock_user_repository)
        user_id = create_user_use_case.execute(user_data)
        self.assertEqual(user_id, 1)


if __name__ == "__main__":
    unittest.main()
