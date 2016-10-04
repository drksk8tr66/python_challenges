"""
This module will contain all item classes and constructors for grabbing the current objects in the 'field of view'
"""


_door = None
# Constructors


def get_door(location):
    if not _door:
        _const_door(location)
    return _door


def _const_door(location):
    global _door
    if not location:
        return "No door in this location."
    descr = location['door'][0]
    door_type = location['door'][1]
    is_locked = location['door'][2]
    _door = Door(descr, door_type, is_locked)


# Classes
class Door:
    def __init__(self, description, door_type, is_locked: bool=False):
        self.description = description
        self.is_locked = is_locked
        self.door_type = door_type

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
        else:
            return "The door is already unlocked"


class Key:
    def __init__(self, key_type):
        self.key_type = key_type

    def use(self):
        if not _door:
            return "No door available to unlock."
        elif _door.door_type == self.key_type:
            _door.unlock()
        elif _door.door_type != self.key_type:
            return "This key cannot open this type of door."


class Potion:
    def __init__(self, potion_type, description):
        self.potion_type = potion_type
        self.description = description

    def use(self):
        if self.potion_type == 'health':
            _char.heal(25)


if __name__ == '__main__':
    _door = Door('A stout wooden door.', 'wood', True)
    print(_door.is_locked)
    _key = Key('wood')
    print(_key.use())
    print(_door.is_locked)
