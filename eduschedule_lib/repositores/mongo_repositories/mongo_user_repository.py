from eduschedule_lib.interfaces.repository import BaseRepository


class MongoUserRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.users_collection = db.users

    def create(self, user, *args, **kwargs):
        new_user = {
            "_login": user["login"],
            "_password": user["password"],
            "_status": user["status"],
            "_student_id": user.get("student_id"),
        }
        result = self.users_collection.insert_one(new_user)
        return result.inserted_id

    def list(self, *args, **kwargs):
        return list(self.users_collection.find())

    def get(self, user_id, *args, **kwargs):
        return self.users_collection.find_one({"_id": user_id})

    def find_by_login(self, login):
        return self.users_collection.find_one({"_login": login})

    def update(self, user, *args, **kwargs):
        pass

    def delete(self, user_id, *args, **kwargs):
        result = self.users_collection.delete_one({"_id": user_id})
        return result.deleted_count > 0

    def delete_by_student_ids(self, student_ids):
        result = self.users_collection.delete_many({"_student_id": {"$in": student_ids}})
        return result.deleted_count
