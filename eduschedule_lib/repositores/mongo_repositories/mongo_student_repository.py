from eduschedule.interfaces.repository import BaseRepository
from eduschedule.repositores.mongo_repositories.mongo_mark_repository import MongoMarkRepository


class MongoStudentRepository(BaseRepository):
    def __init__(self, db, mark_repository: MongoMarkRepository):
        self.db = db
        self.students_collection = db["students"]
        self.mark_repository = mark_repository
        self.next_id = 1

    def list(self, *args, **kwargs):
        return list(self.students_collection.find())

    def get(self, student_id, *args, **kwargs):
        student = self.students_collection.find_one({"_id": student_id})

        if student:
            student_marks = self.mark_repository.list(student_id=student_id)
            return student, student_marks

        return None

    def get_by_group_id(self, group_id, *args, **kwargs):
        students = list(self.students_collection.find({"_group_id": group_id}))
        return students

    def create(self, student, *args, **kwargs):
        new_student_id = self.get_next_id()
        new_student = {
            "_id": new_student_id,
            "_name": student.name,
            "_group_id": student.group_id
        }
        result = self.students_collection.insert_one(new_student)
        return result.inserted_id

    def update(self, student, *args, **kwargs):
        result = self.students_collection.update_one(
            {"_id": student.id},
            {"$set": {
                "_name": student.name,
                "_group_id": student.group_id
            }}
        )
        return result.modified_count > 0

    def delete(self, student_id, *args, **kwargs):
        result = self.students_collection.delete_one({"_id": student_id})
        return result.deleted_count > 0

    def get_next_id(self):
        count = self.students_collection.count_documents({})
        return count + 1 if count > 0 else 1
