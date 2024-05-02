from eduschedule_lib.interfaces.repository import BaseRepository
from eduschedule_lib.domain.schedule import Schedule

class ScheduleRepository(BaseRepository):
    def __init__(self):
        self.schedules = {}
        self.next_id = 1

    def get(self, group_id, *args, **kwargs):
        return self.schedules.get(group_id)

    def create_schedule(self, group_id):
        schedule_id = self.next_id
        new_schedule = Schedule(_id=schedule_id, _group_id=group_id)
        self.schedules[group_id] = new_schedule
        self.next_id += 1
        return new_schedule

    def list(self, *args, **kwargs):
        pass

    def create(self, entity, *args, **kwargs):
        pass

    def update(self, entity):
        pass

    def delete(self, entity_id, *args, **kwargs):
        pass