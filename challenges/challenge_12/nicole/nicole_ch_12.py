"""
Text Adventure Game
https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/

This program creates a maze and allows the user to progress through it
"""

from challenges.challenge_12.nicole import position

if __name__ == "__main__":
    # Using the position class and object to create a maze
    maze = position.Position()

    # Reading coordinates from a text file
    maze.set_coordinates_from_file('maze_coordinates.txt')

    # Displaying the game to the user
    print('You wake up in a cage.  You don\'t remember how you got here.  In front of you is what looks like a maze.  '
          'The maze looks like your only way out.\n')
    maze.default_navigation()
    print('You emerge on the other side of the maze.  You still don\'t know where you are or what happened, but '
          'you\'re glad to be out.')
