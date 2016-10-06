"""
There are two classes defined in this module:

Position: Tracks user movement around a two dimensional grid
    coordinates: A dictionary where the key is a tuple of the x, y coordinate and the value is a tuple of the
        available N/E/S/W directions from the x, y coordinate
    entry_coord: A tuple of the x, y coordinate of maze entry
    exit_coord: A tuple of the x, y coordinate of maze exit
    current_position: A tuple of the x, y coordinate of the current position of the user in the maze
    direction: N/E/S/W direction to go from current_position
    new_position: What the new x, y coordinate tuple would be going "direction" from "current position" (this may or
        may not be a valid position, call validate_position function to determine)
    instructions: List of available commands
    story_valid_direction: Message to display if the user can go in the chosen direction
    story_invalid_direction: Message to display if the user cannot go in the chosen direction

Maze: Subclass of Position that creates a maze game/story
    story_start: The start of the text adventure story to display to the user
    story_end: The end of the text adventure story to display to the user
"""


class Position:
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
        self.story_valid_direction = 'You walk along the path.'
        self.story_invalid_direction = 'There is a wall.'

    def set_coordinates(self, coordinates=None, entry_coord=None, exit_coord=None):
        """
        This function is for setting the coordinates of the maze
        Definitions for each variable are given at the top of this module
        """
        self.coordinates = coordinates
        self.entry_coord = entry_coord
        self.exit_coord = exit_coord
        self.current_position = self.entry_coord

    def set_story_directions(self, story_valid_direction=None, story_invalid_direction=None):
        """
        This function is for setting the directional story elements
        Definitions for each variable are given at the top of this module
        """
        self.story_valid_direction = story_valid_direction
        self.story_invalid_direction = story_invalid_direction

    def change_position(self):
        """
        This function calculates the new x, y coordinate of the user's position after moving in the specified direction
        Definitions for each variable are given at the top of this module
        :return: A tuple of the x, y coordinate of the new position, however, if the direction entered was invalid, the
            new position will equal the old position, and the x, y coordinate will not have changed
        """
        x = self.current_position[0]
        y = self.current_position[1]
        if self.direction.upper() in self.coordinates.get((x, y)):
            if self.direction.upper() == 'N':
                y += 1
            elif self.direction.upper() == 'E':
                x += 1
            elif self.direction.upper() == 'S':
                y -= 1
            elif self.direction.upper() == 'W':
                x -= 1
        return x, y

    def user_interaction(self):
        """
        This function asks the user to enter a command and either quits, moves the user through the maze, or shows an
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
            print(self.story_invalid_direction)
        else:
            print(self.story_valid_direction)
            self.current_position = self.new_position


class Maze(Position):

    def __init__(self):
        """
        Initializing all of the variables to be used throughout this class
        Definitions for each variable are given at the top of this module
        """
        Position.__init__(self)
        self.story_start = 'You wake up in a cage.  You don\'t remember how you got here.  In front of you is what ' \
                           'looks like a maze.  The maze looks like your only way out.\n'
        self.story_end = 'You emerge on the other side of the maze.  You still don\'t know where you are or what ' \
                         'happened, but you\'re glad to be out.'

    def set_story(self, story_start=None, story_end=None):
        """
        This function is for setting the beginning and ending story elements
        Definitions for each variable are given at the top of this module
        """
        self.story_start = story_start
        self.story_end = story_end

    def default_maze(self):
        """
        This function will give the user the default maze if no changes are desired
        Even if using this function, the coordinates will still need to be set in order to contain an actual maze
        Definitions for each variable are given at the top of this module
        """
        print(self.story_start)
        print(self.instructions)
        while self.current_position != self.exit_coord:
            self.user_interaction()
            self.validate_direction()
        print(self.story_end)
