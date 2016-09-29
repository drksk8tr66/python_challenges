# https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/


class Inventory:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = {}

    def add_item(self, name, qty):
        if name in [x for x in self.items]:
            self.items[name] += qty
        elif len(self.items) >= self.size:
            return "Bag is full, unable to add item to inventory"
        else:
            self.items.update({name: qty})

    def drop_item(self, name, qty: int = 1):
        if name in [x for x in self.items]:
            self.items[name] -= qty
        else:
            return "Item not dropped, not found in Inventory"

    def use_item(self, name):
        if name in [x for x in self.items]:
            #call action to use item
            self.drop_item(name, 1)
        else:
            return "Item not used, not found in Inventory"


class Item:
    def __init__(self, name, description, use):
        self.name = name
        self. description = description
        self.use = use


class Door:
    def __init__(self, description, is_locked: bool=False):
        self.description = description
        self.is_locked = is_locked

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
        else:
            return "The door is already unlocked"


class Character:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.inventory = Inventory('bag of holding', 20)
        self.location = location

    def check_inventory(self):
        return self.inventory.items


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        return self.description


if __name__ == '__main__':
    field = Location('field', 'A grassy field with blue wildflowers and a road leading to the North.')
    player_one = Character('Dusty', 'Mild-mannered developer by day, enjoys long walks and dipping his toes in the '
                                    'Putrid Sound by night', field)
    print(player_one.location.look())
    player_one.inventory.add_item('potion', 2)
    player_one.inventory.add_item('sword', 1)
    print(player_one.check_inventory())
