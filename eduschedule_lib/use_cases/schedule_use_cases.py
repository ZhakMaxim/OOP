from eduschedule_lib.repositores.schedule_repository import ScheduleRepository

class GetScheduleUseCase:
    def __init__(self, schedule_repository: ScheduleRepository):
        self.schedule_repository = schedule_repository

    def execute(self, group_id):
        return self.schedule_repository.get(group_id)

