from eduschedule_lib.interfaces.repository import BaseRepository


class MongoGroupRepository(BaseRepository):
    def __init__(self, db, student_repository):
        self.db = db
        self.groups_collection = db.groups
        self.student_repository = student_repository

    def list(self, *args, **kwargs):
        return list(self.groups_collection.find())

    def get(self, group_id, *args, **kwargs):
        return self.groups_collection.find_one({"_id": group_id})

    def create(self, group, *args, **kwargs):
        new_group = {
            "_name": group["name"],
        }
        result = self.groups_collection.insert_one(new_group)
        return result.inserted_id

    def update(self, group):
        result = self.groups_collection.update_one(
            {"_id": group["_id"]},
            {"$set": {
                "_name": group["name"],
            }}
        )
        return result.modified_count > 0

    def delete(self, group_id, *args, **kwargs):
        deleted_students = self.student_repository.delete_by_group_id(group_id)
        result = self.groups_collection.delete_one({"_id": group_id})
        return result.deleted_count > 0
