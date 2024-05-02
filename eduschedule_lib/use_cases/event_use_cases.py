class ListEventsUseCase:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def execute(self):
        return self.event_repository.list()


class GetEventUseCase:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def execute(self, event_id):
        return self.event_repository.get(event_id)


class CreateEventUseCase:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def execute(self, event):
        event_id = self.event_repository.create(event)
        return event_id


class UpdateEventUseCase:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def execute(self, event):
        result = self.event_repository.update(event)
        return result

class DeleteEventUseCase:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def execute(self, event_id):
        result = self.event_repository.delete(event_id)
        return result