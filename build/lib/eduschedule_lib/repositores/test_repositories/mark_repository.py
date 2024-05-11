from eduschedule.interfaces.repository import BaseRepository
from eduschedule.domain.mark import Mark


class MarkRepository(BaseRepository):
    def __init__(self):
        self.marks = {}
        self.next_id = 1

    def list(self, *args, **kwargs):
        return list(self.marks.values())

    def get(self, mark_id, *args, **kwargs):
        return self.marks.get(mark_id)

    def create(self, mark, *args, **kwargs):
        student_id = kwargs.get('student_id')
        if student_id:
            new_mark_id = self.next_id
            new_mark = Mark(_id=new_mark_id,
                            _value=mark.value,
                            _date=mark.date,
                            _student_id=student_id,
                            )
            self.marks[self.next_id] = new_mark
            self.next_id += 1

            return new_mark_id

        return None

    def update(self, mark):
        if mark.id in self.marks:
            self.marks[mark.id] = mark
            return True
        return False

    def delete(self, mark_id, *args, **kwargs):
        if mark_id in self.marks:
            del self.marks[mark_id]
            return True
        return False