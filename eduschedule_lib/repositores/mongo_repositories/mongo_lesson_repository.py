from eduschedule.interfaces.repository import BaseRepository
from eduschedule.domain.lesson import Lesson


class MongoLessonRepository(BaseRepository):
    def __init__(self, db, schedule_repository):
        self.db = db
        self.lessons_collection = db["lessons"]
        self.schedule_repository = schedule_repository

    def create(self, lesson, *args, **kwargs):
        group_id = kwargs.get('group_id')
        schedule = self.schedule_repository.get(group_id)

        if not schedule:
            schedule = self.schedule_repository.create_schedule(group_id)

        new_lesson = {
            "_id": self.get_next_id(),
            "_lesson_name": lesson.lesson_name,
            "_day_of_week": lesson.day_of_week,
            "_start_time": lesson.start_time,
            "_end_time": lesson.end_time,
            "_classroom": lesson.classroom,
            "_schedule_id": schedule.id
        }

        result = self.lessons_collection.insert_one(new_lesson)
        return result.inserted_id

    def list(self, *args, **kwargs):
        return list(self.lessons_collection.find())

    def get(self, lesson_id, *args, **kwargs):
        return self.lessons_collection.find_one({"_id": lesson_id})

    def update(self, lesson):
        update_result = self.lessons_collection.update_one(
            {"_id": lesson.id},
            {"$set": {
                "_lesson_name": lesson.lesson_name,
                "_day_of_week": lesson.day_of_week,
                "_start_time": lesson.start_time,
                "_end_time": lesson.end_time,
                "_classroom": lesson.classroom,
                "_schedule_id": lesson.schedule_id
            }}
        )
        return update_result.modified_count > 0

    def delete(self, lesson_id, *args, **kwargs):
        result = self.lessons_collection.delete_one({"_id": lesson_id})
        return result.deleted_count > 0

    def get_next_id(self):
        count = self.lessons_collection.count_documents({})
        return count + 1 if count > 0 else 1