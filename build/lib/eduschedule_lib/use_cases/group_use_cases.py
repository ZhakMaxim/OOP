from eduschedule_lib.repositores.group_repository import GroupRepository

class CreateGroupUseCase:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def execute(self, group):
        group_id = self.group_repository.create(group)
        return group_id

class GetGroupUseCase:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def execute(self, group_id):
        group = self.group_repository.get(group_id)
        return group

class UpdateGroupUseCase:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def execute(self, group):
        result = self.group_repository.update(group)
        return result

class DeleteGroupUseCase:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def execute(self, group_id):
        result = self.group_repository.delete(group_id)
        return result



