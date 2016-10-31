"""
This loads all of the locations and generates their objects
"""


def get_location(name):
    location = None
    f = open("locations.txt", 'r', newline='')
    line = f.readline().strip('\n\r').split('|')
    if line[0] == name:
        location = Location(line[0], line[1])
        line = f.readline().strip('\n\r').split('|')
        while line != ['']:
            location.add_path(line[0], line[1], line[2], line[3])
            line = f.readline().strip('\n\r').split('|')
        f.close()
        return location
    return "No Location with that name found"


class Location:
    def __init__(self, l_name, description):
        self.name = l_name
        self.description = description
        self.paths = {}

    def look(self, direction: str = 'Around'):
        if direction in [x for x in self.paths]:
            return self.paths[direction].description
        else:
            return self.description

    def add_path(self, direction, description, can_travel, travel_method):
        if direction in self.paths.keys():
            del self.paths[direction]
        self.paths.update({direction: Path(direction, description, can_travel, travel_method)})


class Path:
    default_method = 'There is a wall that blocks your path.'

    def __init__(self, direction, description, can_travel: bool = False, travel_method: str = default_method):
        self.direction = direction
        self.description = description
        self.can_travel = can_travel
        self.travel_method = travel_method


if __name__ == '__main__':
    field = Location('field', 'A grassy field with blue wildflowers and a road leading to the North.')
    field.add_path('n', 'To the North, you see a road.', True, 'A road lays before you.')
    field.add_path('s', 'To the South, you see a cliff face.', False,
                   'The cliff is too tall to scale, you must go another direction.')
    print(field.look('n'))
    print(field.look('s'))
    print(field.look('e'))


