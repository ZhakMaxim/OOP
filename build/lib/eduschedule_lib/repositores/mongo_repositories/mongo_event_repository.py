from eduschedule_lib.interfaces.repository import BaseRepository


class MongoEventRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.events_collection = db.events

    def list(self, *args, **kwargs):
        return list(self.events_collection.find())

    def get(self, event_id, *args, **kwargs):
        return self.events_collection.find_one({"_id": event_id})

    def create(self, event, *args, **kwargs):
        new_event = {
            "_name": event["name"],
            "_description": event["description"],
            "_date": event["date"]
        }
        result = self.events_collection.insert_one(new_event)
        return result.inserted_id

    def update(self, event):
        result = self.events_collection.update_one(
            {"_id": event["_id"]},
            {"$set": {
                "_name": event["name"],
                "_description": event["description"],
                "_date": event["date"],
            }}
        )
        return result.modified_count > 0

    def delete(self, event_id, *args, **kwargs):
        result = self.events_collection.delete_one({"_id": event_id})
        return result.deleted_count > 0
