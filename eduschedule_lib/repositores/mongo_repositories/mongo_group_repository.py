from eduschedule.interfaces.repository import BaseRepository


class MongoGroupRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.groups_collection = db["groups"]

    def list(self, *args, **kwargs):
        return list(self.groups_collection.find())

    def get(self, group_id, *args, **kwargs):
        return self.groups_collection.find_one({"_id": group_id})

    def create(self, group, *args, **kwargs):
        new_group = {
            "_id": group.id,
            "_name": group.name
        }
        result = self.groups_collection.insert_one(new_group)
        return result.inserted_id

    def update(self, group):
        result = self.groups_collection.update_one(
            {"_id": group.id},
            {"$set": {
                "_name": group.name
            }}
        )
        return result.modified_count > 0

    def delete(self, group_id, *args, **kwargs):
        result = self.groups_collection.delete_one({"_id": group_id})
        return result.deleted_count > 0
