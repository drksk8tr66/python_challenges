"""
Position: Tracks user movement around a two dimensional grid
    coordinates: A dictionary where the key is a tuple of the x, y coordinate and the value is a tuple of the
        available N/E/S/W directions in 0s and 1s, respectively, from the x, y coordinate
    entry_coord: A tuple of the x, y coordinate of grid entry
    exit_coord: A tuple of the x, y coordinate of grid exit
    current_position: A tuple of the x, y coordinate of the current position of the user in the grid
    direction: N/E/S/W direction to go from current_position
    new_position: What the new x, y coordinate tuple would be going "direction" from "current position" (this may or
        may not be a valid position, call validate_position function to determine)
    instructions: List of available commands
    valid_direction: Message to display if the user can go in the chosen direction
    invalid_direction: Message to display if the user cannot go in the chosen direction
"""


class Position(object):
    def __init__(self):
        """
        Initializing all of the variables to be used throughout this class
        Definitions for each variable are given at the top of this module
        """
        self.coordinates = {(0, 0): None}
        self.entry_coord = (0, 0)
        self.exit_coord = (0, 0)
        self.current_position = self.entry_coord
        self.direction = None
        self.new_position = None
        self.instructions = 'Available commands:\nQ: quit\nN: go north\nE: go east\nS: go south\nW: go west\n'
        self.valid_direction = 'You walk along the path.'
        self.invalid_direction = 'There is a wall.'

    def set_coordinates(self, coordinates, entry_coord, exit_coord):
        """
        This function is for setting the coordinates of the grid
        Definitions for each variable are given at the top of this module
        """
        self.coordinates = coordinates
        self.entry_coord = entry_coord
        self.exit_coord = exit_coord
        self.current_position = self.entry_coord

    def set_coordinates_from_file(self, file):
        """
        This function is for setting the coordinates of the grid from a file
        Definitions for each variable are given at the top of this module
        The file must be in format:
            x coordinate, y coordinate, int bool north direction, int bool east direction, int bool south direction,
                int bool west direction, entry/exit/interior description
        Example:
        0,0,1,0,0,0,Entry
        0,1,1,0,0,0,Interior
        0,2,0,0,0,0,Exit
        """
        with open(file, 'r') as file:
            for line in file:
                x, y, n, e, s, w, description = line.replace('\n', '').split(',')
                self.coordinates[(int(x), int(y))] = (int(n), int(e), int(s), int(w))
                if description == 'Entry':
                    self.entry_coord = (int(x), int(y))
                    self.current_position = self.entry_coord
                if description == 'Exit':
                    self.exit_coord = (int(x), int(y))

    def set_story_directions(self, valid_direction, invalid_direction):
        """
        This function is for setting the directional story elements
        Definitions for each variable are given at the top of this module
        """
        self.valid_direction = valid_direction
        self.invalid_direction = invalid_direction

    def change_position(self):
        """
        This function calculates the new x, y coordinate of the user's position after moving in the specified direction
        Definitions for each variable are given at the top of this module
        :return: A tuple of the x, y coordinate of the new position, however, if the direction entered was invalid, the
            new position will equal the old position, and the x, y coordinate will not have changed
        """
        x, y = self.current_position
        if self.direction.upper() == 'N' and self.coordinates.get((x, y))[0] == 1:
            y += 1
        elif self.direction.upper() == 'E' and self.coordinates.get((x, y))[1] == 1:
            x += 1
        elif self.direction.upper() == 'S' and self.coordinates.get((x, y))[2] == 1:
            y -= 1
        elif self.direction.upper() == 'W' and self.coordinates.get((x, y))[3] == 1:
            x -= 1
        return x, y

    def user_interaction(self):
        """
        This function asks the user to enter a command and either quits, moves the user through the grid, or shows an
            error for an invalid command
        Definitions for each variable are given at the top of this module
        """
        self.direction = input('Enter command: ').upper()
        if self.direction == 'Q':
            exit()
        elif self.direction in ('N', 'E', 'S', 'W'):
            self.new_position = self.change_position()
        else:
            print('Valid command not entered.')

    def validate_direction(self):
        """
        This function validates the direction that the user entered
        Definitions for each variable are given at the top of this module
        """
        if self.new_position == self.current_position:
            print(self.invalid_direction)
        else:
            print(self.valid_direction)
            self.current_position = self.new_position

    def default_navigation(self):
        """
        This function will allow the user to navigate through the grid
        Definitions for each variable are given at the top of this module
        """
        print(self.instructions)
        while self.current_position != self.exit_coord:
            self.user_interaction()
            self.validate_direction()

