# https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/
from challenges.challenge_12.dustin_ch_12 import items


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
            if self.items[name] <= 0:
                del self.items[name]
        else:
            return "Item not dropped, not found in Inventory"

    def use_item(self, name):
        if name in [x for x in self.items]:
            # call action to use item
            path = 'C:/Users/dust7667/Documents/GitHub/python_challenges/challenges/challenge_12/dustin_ch_12/'
            f = open(path + 'items.txt', 'r', newline='')
            for line in f:
                l = line.split('|')
                if l[0] == name:
                    func = l[2]
                    exec(func)
                    break
            self.drop_item(name, 1)
        else:
            return "Item not used, not found in Inventory"


class Character:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.inventory = Inventory('bag of holding', 20)
        self.location = location
        self.health = 100

    def check_inventory(self):
        return self.inventory.items

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.death()

    def heal(self, amount):
        if self.health + amount >= 100:
            self.health = 100
        else:
            self.health += amount

    def death(self, msg: str = 'You have died'):
        # this is the end of the game, you have died
        print(msg + ", Game Over Man!")
        exit()


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        return self.description


if __name__ == '__main__':
    _door = items.get_door(['A stout wooden door.', 'wood', True])
    field = Location('field', 'A grassy field with blue wildflowers and a road leading to the North.')
    field.add_path
    player_one = Character('Dusty', 'Mild-mannered developer by day, enjoys long walks and dipping his toes in the '
                                    'Putrid Sound by night', field)
    print(player_one.location.look())
    player_one.inventory.add_item('potion', 2)
    player_one.inventory.add_item('sword', 1)
    player_one.inventory.add_item('key', 1)
    print(player_one.check_inventory())
    print(_door.description)
    player_one.inventory.use_item('key')
    print(player_one.check_inventory())
    print(_door.is_locked)
    player_one.take_damage(20)
    print(player_one.health)
    player_one.inventory.use_item('potion')
    print(player_one.check_inventory())
    print(player_one.health)
