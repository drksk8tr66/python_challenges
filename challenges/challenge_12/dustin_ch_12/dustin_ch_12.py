# https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/
from challenges.challenge_12.dustin_ch_12 import items
from challenges.challenge_12.dustin_ch_12 import locations


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
            print("You used a {}.".format(name))
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
        print("This is what is currently in your {}".format(self.inventory.name))
        return self.inventory.items

    def check_health(self):
        return "You are at {} health.".format(self.health)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.death()

    def heal(self, amount):
        c_health = self.health
        if self.health + amount >= 100:
            self.health = 100
        else:
            self.health += amount
        print("You have been healed for {} health".format(self.health - c_health))

    def death(self, msg: str = 'You have died'):
        # this is the end of the game, you have died
        print(msg + ", Game Over Man!")
        exit()


def main():
    print(player_one.location.look())
    print(player_one.location.look('N'))
    print(player_one.location.look('S'))
    print(player_one.location.look('E'))
    print(player_one.location.look('W'))
    player_one.inventory.add_item('potion', 2)
    player_one.inventory.add_item('sword', 1)
    player_one.inventory.add_item('key', 1)
    print(player_one.check_inventory())
    print(_door.description)
    player_one.inventory.use_item('key')
    print(player_one.check_inventory())
    print(_door.is_locked)
    player_one.take_damage(20)
    print(player_one.check_health())
    player_one.inventory.use_item('potion')
    print(player_one.check_inventory())
    print(player_one.check_health())


if __name__ == '__main__':
    _door = items.get_door(['A stout wooden door.', 'wood', True])
    field = locations.get_location('field')
    player_one = Character('Dusty', 'Mild-mannered developer by day, enjoys long walks and dipping his toes in the '
                                    'Putrid Sound by night', field)
    main()

