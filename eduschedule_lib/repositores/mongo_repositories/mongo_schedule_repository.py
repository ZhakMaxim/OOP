from eduschedule.interfaces.repository import BaseRepository
from eduschedule.domain.schedule import Schedule


class MongoScheduleRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.schedules_collection = db["schedules"]

    def get(self, group_id, *args, **kwargs):
        return self.schedules_collection.find_one({"_group_id": group_id})

    def create_schedule(self, group_id):
        new_schedule = {
            "_id": self.get_next_id(),
            "_group_id": group_id
        }
        result = self.schedules_collection.insert_one(new_schedule)
        return Schedule(_id=result.inserted_id, _group_id=group_id)

    def list(self, *args, **kwargs):
        return list(self.schedules_collection.find())

    def create(self, entity, *args, **kwargs):
        pass

    def update(self, entity):
        pass

    def delete(self, entity_id, *args, **kwargs):
        pass

    def get_next_id(self):
        count = self.schedules_collection.count_documents({})
        return count + 1 if count > 0 else 1
