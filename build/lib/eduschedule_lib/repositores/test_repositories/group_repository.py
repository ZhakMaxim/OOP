from eduschedule.interfaces.repository import BaseRepository
from eduschedule.domain.group import Group

class GroupRepository(BaseRepository):
    def __init__(self):
        self.groups = {}
        self.next_id = 1

    def list(self, *args, **kwargs):
        return list(self.groups.values())

    def get(self, group_id, *args, **kwargs):
        return self.groups.get(group_id)

    def create(self, group, *args, **kwargs):
        new_group_id = self.next_id

        new_group = Group(_id=group.id,
                          _name=group.name,
                          )

        self.groups[new_group_id] = new_group
        self.next_id += 1

        return new_group_id

    def update(self, group):
        if group.id in self.groups:
            self.groups[group.id] = group
            return True
        return False

    def delete(self, group_id, *args, **kwargs):
        if group_id in self.groups:
            del self.groups[group_id]
            return True
        return False