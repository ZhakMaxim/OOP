from dataclasses import dataclass

@dataclass(frozen=True)
class Lesson:
    _id: int
    _lesson_name: str
    _day_of_week: str
    _start_time: str
    _end_time: str
    _classroom: str
    _schedule_id: int

    @property
    def id(self):
        return self._id

    @property
    def lesson_name(self):
        return self._lesson_name

    @property
    def day_of_week(self):
        return self._day_of_week

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def classroom(self):
        return self._classroom

    @property
    def schedule_id(self):
        return self._schedule_id

