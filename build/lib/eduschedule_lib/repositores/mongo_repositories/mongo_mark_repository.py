from eduschedule.interfaces.repository import BaseRepository


class MongoMarkRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.marks_collection = db["marks"]
        self.next_id = 1

    def list(self, *args, **kwargs):
        return list(self.marks_collection.find())

    def get(self, mark_id, *args, **kwargs):
        return self.marks_collection.find_one({"_id": mark_id})

    def create(self, mark, *args, **kwargs):
        student_id = kwargs.get('student_id')
        if student_id:
            new_mark = {
                "_id": self.get_next_id(),
                "_value": mark.value,
                "_date": mark.date,
                "_student_id": student_id
            }
            result = self.marks_collection.insert_one(new_mark)
            return result.inserted_id

        return None

    def update(self, mark):
        result = self.marks_collection.update_one(
            {"_id": mark.id},
            {"$set": {
                "_value": mark.value,
                "_date": mark.date,
                "_student_id": mark.student_id
            }}
        )
        return result.modified_count > 0

    def delete(self, mark_id, *args, **kwargs):
        result = self.marks_collection.delete_one({"_id": mark_id})
        return result.deleted_count > 0

    def get_next_id(self):
        count = self.marks_collection.count_documents({})
        return count + 1 if count > 0 else 1
