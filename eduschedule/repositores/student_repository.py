from eduschedule.interfaces.repository import BaseRepository
from eduschedule.domain.student import Student
from eduschedule.repositores.mark_repository import MarkRepository


class StudentRepository(BaseRepository):
    def __init__(self, mark_repository: MarkRepository):
        self.students = {}
        self.mark_repository = mark_repository
        self.next_id = 1

    def list(self, *args, **kwargs):
        pass

    def get(self, student_id, *args, **kwargs):
        student = self.students.get(student_id)

        if student:
            student_marks = [mark for mark in self.mark_repository.list() if mark.student_id == student_id]

            return student, student_marks

        return None

    def create(self, student, *args, **kwargs):
        new_student_id = self.next_id
        new_student = Student(_id=new_student_id,
                              _name=student.name,
                              _group_id=student.group_id,
                              )
        self.students[new_student_id] = new_student
        self.next_id += 1
        return new_student_id

    def update(self, student, *args, **kwargs):
        if student.id in self.students:
            self.students[student.id] = student
            return True
        return False

    def delete(self, student_id, *args, **kwargs):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
