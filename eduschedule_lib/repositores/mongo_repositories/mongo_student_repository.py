from eduschedule_lib.interfaces.repository import BaseRepository
from eduschedule_lib.repositores.mongo_repositories.mongo_mark_repository import MongoMarkRepository


class MongoStudentRepository(BaseRepository):
    def __init__(self, db, mark_repository: MongoMarkRepository, user_repository):
        self.db = db
        self.students_collection = db.students
        self.mark_repository = mark_repository
        self.user_repository = user_repository

    def list(self, *args, **kwargs):
        return list(self.students_collection.find())

    def get(self, student_id, *args, **kwargs):
        student = self.students_collection.find_one({"_id": student_id})

        if student:
            student_marks = self.mark_repository.get_by_student_id(str(student_id))
            student_with_marks = {
                "student": student,
                "marks": student_marks
            }
            return student_with_marks

        return None

    def get_by_group_id(self, group_id, *args, **kwargs):
        students = list(self.students_collection.find({"_group_id": group_id}))
        students_with_marks = []

        for student in students:
            student_id = student["_id"]
            student_marks = self.mark_repository.get_by_student_id(str(student_id))
            student_with_marks = {
                "student": student,
                "marks": student_marks
            }
            students_with_marks.append(student_with_marks)

        return students_with_marks

    def create(self, student, *args, **kwargs):
        new_student = {
            "_name": student["name"],
            "_group_id": student["group_id"],
        }
        result = self.students_collection.insert_one(new_student)
        return result.inserted_id

    def update(self, student, *args, **kwargs):
        result = self.students_collection.update_one(
            {"_id": student["_id"]},
            {"$set": {
                "_name": student["name"],
                "_group_id": student["group_id"],
            }}
        )
        return result.modified_count > 0

    def delete(self, student_id, *args, **kwargs):
        deleted_marks = self.mark_repository.delete_by_student_id(student_id)
        result = self.students_collection.delete_one({"_id": student_id})
        return result.deleted_count > 0

    def delete_by_group_id(self, group_id, *args, **kwargs):
        students = self.students_collection.find({"_group_id": group_id})
        student_ids = [student["_id"] for student in students]

        self.user_repository.delete_by_student_ids(student_ids)

        result = self.students_collection.delete_many({"_group_id": group_id})
        return result.deleted_count > 0