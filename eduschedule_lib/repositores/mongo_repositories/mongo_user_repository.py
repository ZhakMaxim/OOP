from eduschedule.interfaces.repository import BaseRepository


class MongoUserRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.users_collection = db["users"]
        self.next_id = 1

    def create(self, user, *args, **kwargs):
        new_user_id = self.get_next_id()
        new_user = {
            "_id": new_user_id,
            "_login": user.login,
            "_password": user.password,
            "_status": user.status,
            "_student_id": user.student_id
        }
        result = self.users_collection.insert_one(new_user)
        return result.inserted_id

    def list(self, *args, **kwargs):
        return list(self.users_collection.find())

    def get(self, user_id, *args, **kwargs):
        return self.users_collection.find_one({"_id": user_id})

    def update(self, user, *args, **kwargs):
        result = self.users_collection.update_one(
            {"_id": user.id},
            {"$set": {
                "_login": user.login,
                "_password": user.password,
                "_status": user.status,
                "_student_id": user.student_id
            }}
        )
        return result.modified_count > 0

    def delete(self, user_id, *args, **kwargs):
        result = self.users_collection.delete_one({"_id": user_id})
        return result.deleted_count > 0

    def get_next_id(self):
        count = self.users_collection.count_documents({})
        return count + 1 if count > 0 else 1
