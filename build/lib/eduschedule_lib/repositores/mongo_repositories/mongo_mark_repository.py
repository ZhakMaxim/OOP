from eduschedule_lib.interfaces.repository import BaseRepository
from datetime import datetime

class MongoMarkRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.marks_collection = db.marks

    def list(self, *args, **kwargs):
        return list(self.marks_collection.find())

    def get(self, mark_id, *args, **kwargs):
        return self.marks_collection.find_one({"_id": mark_id})

    def get_by_student_id(self, student_id, *args, **kwargs):
        return list(self.marks_collection.find({"_student_id": student_id}))

    def create(self, mark, *args, **kwargs):
        new_mark = {
            "_value": mark["value"],
            "_date": mark["date"],
            "_subject": mark["subject"],
            "_student_id": mark["student_id"],
        }
        result = self.marks_collection.insert_one(new_mark)
        return result.inserted_id


    def update(self, mark):
        result = self.marks_collection.update_one(
            {"_id": mark["_id"]},
            {"$set": {
                "_value": mark["value"],
                "_date": datetime.now(),
                "_student_id": mark["student_id"],
            }}
        )
        return result.modified_count > 0

    def delete(self, mark_id, *args, **kwargs):
        result = self.marks_collection.delete_one({"_id": mark_id})
        return result.deleted_count > 0

    def delete_by_student_id(self, student_id, *args, **kwargs):
        result = self.marks_collection.delete_many({"_student_id": student_id})
        return result.deleted_count > 0