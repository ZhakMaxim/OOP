from eduschedule.interfaces.repository import BaseRepository
from eduschedule.domain.event import Event


class EventRepository(BaseRepository):
    def __init__(self):
        self.events = {}
        self.next_id = 1

    def list(self, *args, **kwargs):
        return list(self.events.values())

    def get(self, event_id, *args, **kwargs):
        return self.events.get(event_id)

    def create(self, event, *args, **kwargs):
        new_event_id = self.next_id
        new_event = Event(_id=new_event_id, _name=event.name, _description=event.description, _date=event.date)
        self.events[new_event_id] = new_event
        self.next_id += 1
        return new_event_id

    def update(self, event):
        if event.id in self.events:
            self.events[event.id] = event
            return True
        return False

    def delete(self, event_id, *args, **kwargs):
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False
