from eduschedule.interfaces.repository import BaseRepository
from eduschedule.repositores.test_repositories.schedule_repository import ScheduleRepository
from eduschedule.domain.lesson import Lesson


class LessonRepository(BaseRepository):
    def __init__(self, schedule_repository: ScheduleRepository):
        self.next_id = 1
        self.lessons = {}
        self.schedule_repository = schedule_repository

    def create(self, lesson, *args, **kwargs):
        group_id = kwargs.get('group_id')
        new_lesson_id = self.next_id

        schedule = self.schedule_repository.get(group_id)

        if not schedule:
            schedule = self.schedule_repository.create_schedule(group_id)

        new_lesson = Lesson(_id=new_lesson_id,
                            _lesson_name=lesson.lesson_name,
                            _day_of_week=lesson.day_of_week,
                            _start_time=lesson.start_time,
                            _end_time=lesson.end_time,
                            _classroom=lesson.classroom,
                            _schedule_id=schedule.id,
                            )

        self.lessons[new_lesson_id] = new_lesson
        self.next_id += 1

        return new_lesson_id

    def list(self, *args, **kwargs):
        pass

    def get(self, lesson_id, *args, **kwargs):
        schedule_id = kwargs.get('schedule_id')

        if schedule_id is not None:
            schedule = self.schedule_repository.get(schedule_id)

            if schedule:
                for lesson in schedule.lessons:
                    if lesson.id == lesson_id:
                        return lesson

        return None

    def update(self, lesson):
        schedule = self.schedule_repository.get(lesson.schedule_id)

        if schedule:
            for idx, existing_lesson in enumerate(schedule.lessons):
                if existing_lesson.id == lesson.id:
                    schedule.lessons[idx] = lesson
                    return True

        return False

    def delete(self, lesson_id, *args, **kwargs):
        schedule_id = kwargs.get('schedule_id')
        schedule = self.schedule_repository.get(schedule_id)

        if schedule:
            schedule.lessons = [lesson for lesson in schedule.lessons if lesson.id != lesson_id]
            return True

        return False
