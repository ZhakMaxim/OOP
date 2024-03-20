import unittest

from user_use_cases_tests import TestUserUseCases
from student_use_cases_tests import TestStudentUseCases
from schedule_use_cases_tests import TestScheduleUseCases
from mark_use_cases_tests import TestMarkUseCases
from lesson_use_cases_tests import TestLessonUseCases
from group_use_cases_tests import TestGroupUseCases
from event_use_cases_tests import TestEventUseCases

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTest(loader.loadTestsFromTestCase(TestUserUseCases))
    suite.addTest(loader.loadTestsFromTestCase(TestStudentUseCases))
    suite.addTest(loader.loadTestsFromTestCase(TestScheduleUseCases))
    suite.addTest(loader.loadTestsFromTestCase(TestMarkUseCases))
    suite.addTest(loader.loadTestsFromTestCase(TestLessonUseCases))
    suite.addTest(loader.loadTestsFromTestCase(TestGroupUseCases))
    suite.addTest(loader.loadTestsFromTestCase(TestEventUseCases))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
